# Moon Spot - Quick Start Guide

## 🚀 What is Moon Spot?

Moon Spot is a custom-branded version of Batocera Linux designed for arcade kiosk deployments. It includes:

- **Kiosk Mode** - Locked-down configuration to prevent user tampering
- **Monthly ROM Rotation** - Easy ROM management with monthly game collections
- **High Score Tracking** - RetroAchievements integration for leaderboards
- **Digital Signage** - Display promotional content on a second screen
- **Web Admin Panel** - Manage everything from a browser

## 🎮 Building Your First Moon Spot Image

### Prerequisites

- Linux build machine (Ubuntu 20.04+ recommended)
- At least 50GB free disk space
- 8GB+ RAM
- Good internet connection

### Step 1: Configure Build

```bash
cd batocera.linux

# Configure for x86_64 (PC)
make batocera-moonspot-x86_64-config

# Or manually configure
make menuconfig
# Navigate to: System -> Moon Spot Packages -> Enable all
```

### Step 2: Add Your Branding

Before building, add your Moon Spot branded assets:

```bash
# Copy your logo (1920x1080 PNG)
cp /path/to/your/logo.png \
   package/batocera/moonspot/moonspot-splash/images/logo.png

# Copy your splash video (keep it short, <10 seconds)
cp /path/to/your/splash.mp4 \
   package/batocera/moonspot/moonspot-splash/videos/splash.mp4

# Add screensaver content
mkdir -p package/batocera/moonspot/moonspot-splash/videos/screensaver
cp /path/to/your/promos/*.mp4 \
   package/batocera/moonspot/moonspot-splash/videos/screensaver/
```

### Step 3: Build

```bash
# Start the build (this will take 1-2 hours)
make

# The image will be created in:
# output/images/batocera/batocera-*.img
```

### Step 4: Flash to USB/SD

```bash
# Find your device (e.g., /dev/sdb)
lsblk

# Flash the image
sudo dd if=output/images/batocera/batocera-*.img \
        of=/dev/sdX \
        bs=4M \
        status=progress

# Sync and eject
sync
```

## 📦 Preparing ROM Packages

### Create ROM Package Structure

```bash
mkdir -p roms-2025-01/{snes,genesis,arcade}

# Copy ROMs
cp *.smc roms-2025-01/snes/
cp *.md roms-2025-01/genesis/
cp *.zip roms-2025-01/arcade/

# Create manifest
cat > roms-2025-01/manifest.json << EOF
{
  "month": "2025-01",
  "name": "January 2025 - Classic Collection",
  "description": "Best games from the 90s",
  "systems": {
    "snes": ["game1.smc", "game2.smc"],
    "genesis": ["sonic.md", "streets-of-rage.md"],
    "arcade": ["pacman.zip", "galaga.zip"]
  }
}
EOF

# Create package
tar -czf roms-2025-01.tar.gz -C roms-2025-01 .
```

## 🖥️ Initial System Setup

### First Boot

1. **Boot from USB/SD card**
2. **Wait for Moon Spot splash screen**
3. **Note the IP address** displayed at boot

### Access Admin Panel

1. **Open browser:** `http://<moonspot-ip>:8080`
2. **Configure RetroAchievements:**
   - Username: Your retroachievements.org username
   - Password: Your password
   - Enable: ✓

3. **Upload ROM Package:**
   - Click "Choose File"
   - Select `roms-2025-01.tar.gz`
   - Click "Activate Selected Month"

4. **Configure Digital Signage (if using second screen):**
   - Upload promotional videos
   - Set rotation interval
   - Enable signage

### Enable Kiosk Mode

Kiosk mode is **enabled by default**. Settings are locked to prevent user changes.

To make changes:
1. Disable kiosk mode in admin panel
2. Make your changes
3. Re-enable kiosk mode

## 🏆 RetroAchievements Setup

### Get Account

1. Create account at: https://retroachievements.org
2. Note your username and password

### Configure in Moon Spot

**Via Web Interface:**
1. Open admin panel
2. Navigate to "High Score Tracking"
3. Enter credentials
4. Save

**Via SSH (if enabled):**
```bash
# Edit moonspot config
nano /userdata/system/moonspot/moonspot.conf

# Set credentials
RETROACHIEVEMENTS_USER="your_username"
RETROACHIEVEMENTS_PASSWORD="your_password"

# Restart kiosk service
/etc/init.d/S99moonspot-kiosk restart
```

## 📺 Digital Signage Setup

### Connect Second Display

1. **Connect HDMI to second output**
2. **Detect displays:**
   ```bash
   moonspot-signage detect
   ```

3. **Configure display:**
   ```bash
   nano /userdata/system/moonspot/signage.conf
   ```

   Set:
   ```bash
   MOONSPOT_SIGNAGE_DISPLAY="HDMI-2"  # or detected display name
   ROTATION_INTERVAL=30
   LOOP=true
   ```

### Add Content

**Via Command Line:**
```bash
moonspot-signage add /path/to/video.mp4
moonspot-signage add /path/to/image.jpg
```

**Via Web Interface:**
- Coming soon: Upload via admin panel

### Start Signage

```bash
moonspot-signage start

# Or enable at boot
nano /userdata/system/moonspot/signage.conf
# Set: MOONSPOT_SIGNAGE_ENABLED=1
```

## 🔄 Monthly ROM Rotation

### Manual Update

1. **Create new month package** (e.g., `roms-2025-02.tar.gz`)
2. **Open admin panel**
3. **Select new month**
4. **Upload package**
5. **Click "Activate Selected Month"**
6. **System will reload EmulationStation**

### Command Line Update

```bash
# Upload package to system
scp roms-2025-02.tar.gz root@moonspot:/tmp/

# SSH to system
ssh root@moonspot

# Move to ROM directory
mkdir -p /userdata/system/moonspot/roms/2025-02
tar -xzf /tmp/roms-2025-02.tar.gz \
    -C /userdata/system/moonspot/roms/2025-02

# Activate
moonspot-rom-manager activate 2025-02
```

## 🔧 Common Tasks

### Restart Services

```bash
# Restart kiosk mode
/etc/init.d/S99moonspot-kiosk restart

# Restart backend API
/etc/init.d/S95moonspot-backend restart

# Restart digital signage
/etc/init.d/S96moonspot-signage restart
```

### View Logs

```bash
# EmulationStation logs
tail -f /userdata/system/logs/es_log.txt

# Backend API logs
journalctl -u moonspot-backend -f

# System logs
dmesg | tail -50
```

### Backup Configuration

```bash
# Backup everything
tar -czf moonspot-backup-$(date +%Y%m%d).tar.gz \
    /userdata/system/moonspot \
    /userdata/system/batocera.conf

# Restore
tar -xzf moonspot-backup-YYYYMMDD.tar.gz -C /
```

## 📱 Network Access

### Admin Panel
- URL: `http://moonspot:8080` or `http://<ip>:8080`

### SSH Access (if enabled)
```bash
ssh root@moonspot
# Default password: linux
```

### File Sharing (if enabled)
- Windows: `\\moonspot\share`
- Mac/Linux: `smb://moonspot/share`

## 🎯 Best Practices

### ROM Selection
- Choose 10-15 games per month
- Mix popular classics with hidden gems
- Include variety of genres
- Test all games before deployment

### High Scores
- Create competition themes
- Announce monthly winners
- Display top scores on signage
- Reset scores monthly for fair competition

### Content Updates
- Update signage content weekly
- Match signage to current ROM selection
- Include game tips and tricks
- Promote upcoming events

### Maintenance
- Check system weekly
- Monitor disk space
- Update ROMs monthly
- Clean/reboot system monthly

## ❓ Troubleshooting

### ROMs Don't Appear
```bash
# Check ROM directory
ls -R /userdata/roms/

# Refresh EmulationStation
killall -HUP emulationstation
```

### Signage Not Working
```bash
# Detect displays
moonspot-signage detect

# Check media files
moonspot-signage list

# Restart signage
moonspot-signage restart
```

### Admin Panel Not Accessible
```bash
# Check service status
/etc/init.d/S95moonspot-backend status

# Restart service
/etc/init.d/S95moonspot-backend restart

# Check IP address
ip addr show
```

### Settings Keep Resetting
This is normal in kiosk mode! To make permanent changes:
```bash
# Via web: Disable kiosk mode → Make changes → Update master → Re-enable

# Via command line:
chattr -i /userdata/system/batocera.conf
# Make changes
moonspot-settings-guard update-master
chattr +i /userdata/system/batocera.conf
```

## 📚 Additional Resources

- **Batocera Wiki:** https://wiki.batocera.org
- **RetroAchievements:** https://retroachievements.org
- **EmulationStation:** https://emulationstation.org
- **Moon Spot Full Docs:** See `package/batocera/moonspot/README.md`

## 🎉 You're Ready!

Your Moon Spot arcade kiosk is now configured and ready to provide an amazing retro gaming experience!

Enjoy! 🚀🎮
