#!/usr/bin/env python3
"""
Moon Spot Backend API
Manages ROM rotation, high scores, and kiosk configuration
"""

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import os
import json
import subprocess
from datetime import datetime
import logging

app = Flask(__name__)
CORS(app)

# Configuration
MOONSPOT_DATA = "/userdata/system/moonspot"
ROMS_DIR = f"{MOONSPOT_DATA}/roms"
CONFIG_FILE = f"{MOONSPOT_DATA}/config.json"
BATOCERA_CONF = "/userdata/system/batocera.conf"

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Helper functions
def load_config():
    """Load Moon Spot configuration"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {
        "current_month": datetime.now().strftime("%Y-%m"),
        "retroachievements": {},
        "kiosk_enabled": True
    }


def save_config(config):
    """Save Moon Spot configuration"""
    os.makedirs(MOONSPOT_DATA, exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)


def get_batocera_setting(key):
    """Get a setting from batocera.conf"""
    try:
        result = subprocess.run(
            ['batocera-settings-get', key],
            capture_output=True, text=True
        )
        return result.stdout.strip()
    except Exception as e:
        logger.error(f"Error getting setting {key}: {e}")
        return None


def set_batocera_setting(key, value):
    """Set a setting in batocera.conf"""
    try:
        subprocess.run(
            ['batocera-settings-set', key, value],
            check=True
        )
        return True
    except Exception as e:
        logger.error(f"Error setting {key}={value}: {e}")
        return False


# API Routes

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "ok",
        "service": "moonspot-backend",
        "version": "1.0"
    })


@app.route('/api/config', methods=['GET'])
def get_config():
    """Get current Moon Spot configuration"""
    config = load_config()
    return jsonify(config)


@app.route('/api/config', methods=['POST'])
def update_config():
    """Update Moon Spot configuration"""
    try:
        config = load_config()
        data = request.json

        # Update configuration
        config.update(data)
        save_config(config)

        return jsonify({
            "status": "success",
            "config": config
        })
    except Exception as e:
        logger.error(f"Error updating config: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/roms/month/<month_id>', methods=['GET'])
def get_month_roms(month_id):
    """Get ROM list for a specific month"""
    try:
        rom_file = f"{ROMS_DIR}/{month_id}/manifest.json"

        if os.path.exists(rom_file):
            with open(rom_file, 'r') as f:
                return jsonify(json.load(f))
        else:
            return jsonify({
                "month": month_id,
                "systems": {},
                "message": "No ROMs configured for this month"
            })
    except Exception as e:
        logger.error(f"Error getting ROMs for {month_id}: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/roms/upload', methods=['POST'])
def upload_roms():
    """Upload ROM package for a month"""
    try:
        month_id = request.form.get('month_id', datetime.now().strftime("%Y-%m"))
        file = request.files.get('rom_package')

        if not file:
            return jsonify({"status": "error", "message": "No file provided"}), 400

        # Create month directory
        month_dir = f"{ROMS_DIR}/{month_id}"
        os.makedirs(month_dir, exist_ok=True)

        # Save uploaded file
        package_path = f"{month_dir}/roms.tar.gz"
        file.save(package_path)

        # Extract package
        subprocess.run(['tar', '-xzf', package_path, '-C', month_dir], check=True)

        return jsonify({
            "status": "success",
            "month": month_id,
            "message": "ROM package uploaded successfully"
        })
    except Exception as e:
        logger.error(f"Error uploading ROMs: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/roms/download/<month_id>', methods=['GET'])
def download_roms(month_id):
    """Download ROM package for a month"""
    try:
        package_path = f"{ROMS_DIR}/{month_id}/roms.tar.gz"

        if os.path.exists(package_path):
            return send_file(package_path, as_attachment=True)
        else:
            return jsonify({
                "status": "error",
                "message": f"ROM package for {month_id} not found"
            }), 404
    except Exception as e:
        logger.error(f"Error downloading ROMs: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/roms/activate/<month_id>', methods=['POST'])
def activate_roms(month_id):
    """Activate ROM set for a specific month"""
    try:
        # Call moonspot-rom-manager to activate
        result = subprocess.run(
            ['moonspot-rom-manager', 'activate', month_id],
            capture_output=True, text=True, check=True
        )

        # Update config
        config = load_config()
        config['current_month'] = month_id
        save_config(config)

        return jsonify({
            "status": "success",
            "month": month_id,
            "message": "ROM set activated"
        })
    except Exception as e:
        logger.error(f"Error activating ROMs: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/settings/kiosk', methods=['GET'])
def get_kiosk_status():
    """Get kiosk mode status"""
    menu_mode = get_batocera_setting('system.es.menu')
    ssh_enabled = get_batocera_setting('system.ssh.enabled')

    return jsonify({
        "kiosk_enabled": menu_mode == "bartop",
        "ssh_enabled": ssh_enabled == "1",
        "menu_mode": menu_mode
    })


@app.route('/api/settings/kiosk', methods=['POST'])
def update_kiosk_settings():
    """Update kiosk mode settings"""
    try:
        data = request.json
        enabled = data.get('enabled', True)

        # Temporarily remove immutable flag
        subprocess.run(['chattr', '-i', BATOCERA_CONF], check=False)

        if enabled:
            set_batocera_setting('system.es.menu', 'bartop')
            set_batocera_setting('system.ssh.enabled', '0')
        else:
            set_batocera_setting('system.es.menu', 'default')
            set_batocera_setting('system.ssh.enabled', '1')

        # Restore immutable flag if kiosk enabled
        if enabled:
            subprocess.run(['chattr', '+i', BATOCERA_CONF], check=False)

        return jsonify({
            "status": "success",
            "kiosk_enabled": enabled
        })
    except Exception as e:
        logger.error(f"Error updating kiosk settings: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/achievements/config', methods=['GET'])
def get_achievements_config():
    """Get RetroAchievements configuration"""
    config = load_config()
    return jsonify(config.get('retroachievements', {}))


@app.route('/api/achievements/config', methods=['POST'])
def update_achievements_config():
    """Update RetroAchievements configuration"""
    try:
        data = request.json
        config = load_config()

        # Update RetroAchievements settings
        config['retroachievements'] = data

        # Temporarily remove immutable flag
        subprocess.run(['chattr', '-i', BATOCERA_CONF], check=False)

        if data.get('enabled'):
            set_batocera_setting('global.retroachievements', '1')
            set_batocera_setting('global.retroachievements.username', data.get('username', ''))
            set_batocera_setting('global.retroachievements.password', data.get('password', ''))
            set_batocera_setting('global.retroachievements.leaderboards', '1')
        else:
            set_batocera_setting('global.retroachievements', '0')

        # Restore immutable flag
        subprocess.run(['chattr', '+i', BATOCERA_CONF], check=False)

        save_config(config)

        return jsonify({
            "status": "success",
            "config": config['retroachievements']
        })
    except Exception as e:
        logger.error(f"Error updating achievements config: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/system/reboot', methods=['POST'])
def reboot_system():
    """Reboot the system"""
    try:
        subprocess.Popen(['shutdown', '-r', 'now'])
        return jsonify({"status": "success", "message": "System rebooting..."})
    except Exception as e:
        logger.error(f"Error rebooting: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/system/shutdown', methods=['POST'])
def shutdown_system():
    """Shutdown the system"""
    try:
        subprocess.Popen(['shutdown', '-h', 'now'])
        return jsonify({"status": "success", "message": "System shutting down..."})
    except Exception as e:
        logger.error(f"Error shutting down: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    # Ensure data directory exists
    os.makedirs(MOONSPOT_DATA, exist_ok=True)
    os.makedirs(ROMS_DIR, exist_ok=True)

    # Start the API server
    app.run(host='0.0.0.0', port=8080, debug=False)
