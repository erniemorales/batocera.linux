# Moon Spot - Branded Batocera Arcade Kiosk

Moon Spot is a branded version of Batocera Linux designed for arcade kiosk deployments with monthly ROM rotation, high score tracking, and digital signage support.

## Features

### 🎮 Kiosk Mode
- **Locked settings** - Prevents users from modifying system configuration
- **Simplified menu** - Bartop-style menu with minimal options
- **Automatic protection** - Settings are restored if tampered with
- **Secure access** - SSH and Samba disabled by default

### 🎯 Monthly ROM Rotation
- **Backend management** - Web-based ROM upload and activation
- **Automatic scheduling** - ROMs can be rotated monthly
- **Version control** - Multiple ROM sets can be stored and activated
- **Easy deployment** - Upload tar.gz packages via web interface

### 🏆 High Score Tracking
- **RetroAchievements integration** - Track scores across multiple games
- **Leaderboards** - Compete for the best scores
- **Achievement notifications** - Visual feedback for accomplishments
- **Centralized management** - Configure via web interface

### 📺 Digital Signage
- **Second screen support** - Display promotional content on additional monitors
- **Media rotation** - Automatically cycle through videos and images
- **Hardware accelerated** - Smooth playback using GPU
- **Easy content management** - Add/remove media via API or command line

### 🎨 Custom Branding
- **Custom splash screens** - Moon Spot branded boot animation
- **Themed interface** - Custom EmulationStation appearance
- **Logo integration** - Moon Spot branding throughout the system

### 🔧 Backend Management
- **Web interface** - Admin panel for all configuration
- **REST API** - Programmatic control of all features
- **Remote management** - Configure from any device on the network
- **System control** - Reboot/shutdown capabilities

## Directory Structure

```
package/batocera/moonspot/
├── Config.in                       # Package menu configuration
├── moonspot-splash/                # Splash screen and branding
│   ├── images/                     # Logo images
│   ├── videos/                     # Boot and screensaver videos
│   └── moonspot-splash.mk
├── moonspot-kiosk/                 # Kiosk mode and ROM management
│   ├── scripts/
│   │   ├── moonspot-kiosk-init     # Kiosk initialization
│   │   ├── moonspot-settings-guard # Settings protection
│   │   └── moonspot-rom-manager    # ROM rotation manager
│   └── moonspot-kiosk.mk
├── moonspot-backend/               # Backend API and web UI
│   ├── api/
│   │   └── moonspot-api.py         # Flask REST API
│   ├── web/
│   │   └── index.html              # Admin web interface
│   └── moonspot-backend.mk
└── moonspot-signage/               # Digital signage
    ├── scripts/
    │   ├── moonspot-signage        # Signage control script
    │   └── S96moonspot-signage     # Init script
    └── moonspot-signage.mk
```

## Installation

### Building Moon Spot Image

1. **Clone the repository** (already done)

2. **Configure the build:**
   ```bash
   cd batocera.linux
   make batocera-moonspot-x86_64-config
   ```

3. **Build the image:**
   ```bash
   make
   ```

4. **Flash to USB/SD card:**
   ```bash
   dd if=output/images/batocera/batocera-moonspot-x86_64-XXXXX-XXXXXX.img of=/dev/sdX bs=4M
   ```

### Adding Custom Branding

Place your Moon Spot branded assets:

**Splash Images:**
- `package/batocera/moonspot/moonspot-splash/images/logo.png`
- `package/batocera/moonspot/moonspot-splash/images/logo-480p.png`

**Splash Video:**
- `package/batocera/moonspot/moonspot-splash/videos/splash.mp4`

**Screensaver Videos:**
- `package/batocera/moonspot/moonspot-splash/videos/screensaver/*.mp4`

## Configuration

### Initial Setup

1. **Boot the Moon Spot system**

2. **Access the admin panel:**
   - Navigate to `http://moonspot:8080` or `http://<ip-address>:8080`
   - Default credentials: none (local access only)

3. **Configure RetroAchievements:**
   - Enter your RetroAchievements username and password
   - Enable high score tracking

4. **Upload ROMs:**
   - Select the current month
   - Upload a ROM package (.tar.gz)
   - Activate the ROM set

5. **Configure Digital Signage:**
   - Add promotional videos/images
   - Set rotation intervals
   - Enable on second screen

### ROM Package Structure

Create ROM packages in this format:

```
roms-2025-01.tar.gz
├── manifest.json
├── snes/
│   ├── game1.smc
│   ├── game2.smc
│   └── gamelist.xml
├── genesis/
│   ├── game1.md
│   ├── game2.md
│   └── gamelist.xml
└── arcade/
    ├── game1.zip
    ├── game2.zip
    └── gamelist.xml
```

**manifest.json example:**
```json
{
  "month": "2025-01",
  "name": "January 2025 Collection",
  "systems": {
    "snes": ["game1.smc", "game2.smc"],
    "genesis": ["game1.md", "game2.md"],
    "arcade": ["game1.zip", "game2.zip"]
  }
}
```

## Usage

### ROM Management

**Via Web Interface:**
1. Open admin panel: `http://moonspot:8080`
2. Select month in ROM Management section
3. Upload ROM package
4. Click "Activate Selected Month"

**Via Command Line:**
```bash
# Download ROM set for current month
moonspot-rom-manager download

# Activate a specific month
moonspot-rom-manager activate 2025-01

# List available ROM sets
moonspot-rom-manager list
```

### Digital Signage

**Add media:**
```bash
moonspot-signage add /path/to/video.mp4
```

**List media:**
```bash
moonspot-signage list
```

**Start/stop signage:**
```bash
moonspot-signage start
moonspot-signage stop
```

### Kiosk Mode

Kiosk mode is enabled by default. To temporarily disable for maintenance:

```bash
# Remove settings protection
chattr -i /userdata/system/batocera.conf

# Make changes...

# Re-enable protection
chattr +i /userdata/system/batocera.conf
```

Or use the web interface to toggle kiosk mode.

## API Reference

### Base URL
`http://moonspot:8080/api`

### Endpoints

**Configuration**
- `GET /config` - Get current configuration
- `POST /config` - Update configuration

**ROM Management**
- `GET /roms/month/<month_id>` - Get ROM list for month
- `POST /roms/upload` - Upload ROM package
- `GET /roms/download/<month_id>` - Download ROM package
- `POST /roms/activate/<month_id>` - Activate ROM set

**Kiosk Settings**
- `GET /settings/kiosk` - Get kiosk status
- `POST /settings/kiosk` - Update kiosk settings

**RetroAchievements**
- `GET /achievements/config` - Get achievement configuration
- `POST /achievements/config` - Update achievement settings

**System Control**
- `POST /system/reboot` - Reboot system
- `POST /system/shutdown` - Shutdown system

## Troubleshooting

### ROMs not appearing
1. Check ROM package structure matches expected format
2. Verify manifest.json is valid
3. Check EmulationStation logs: `/userdata/system/logs/es_log.txt`

### Signage not displaying
1. Verify second display is connected and detected:
   ```bash
   moonspot-signage detect
   ```
2. Check media files are in correct directory:
   ```bash
   moonspot-signage list
   ```
3. Verify display configuration in `/userdata/system/moonspot/signage.conf`

### Web interface not accessible
1. Check backend service is running:
   ```bash
   /etc/init.d/S95moonspot-backend status
   ```
2. Restart backend:
   ```bash
   /etc/init.d/S95moonspot-backend restart
   ```
3. Check firewall settings

### Settings being reset
This is expected behavior in kiosk mode. To make permanent changes:
1. Access web interface
2. Disable kiosk mode temporarily
3. Make changes
4. Update master configuration:
   ```bash
   moonspot-settings-guard update-master
   ```
5. Re-enable kiosk mode

## Credits

Moon Spot is built on [Batocera Linux](https://batocera.org), an open-source retro-gaming distribution.

**Artwork:** Based on the provided Moon Spot branding (rocket logo and robot mascot)

**Technologies:**
- Batocera Linux
- EmulationStation
- RetroArch
- Python Flask
- MPV Media Player

## License

Moon Spot customizations are provided as-is. Batocera Linux and its components retain their original licenses.

## Support

For issues and questions:
- Check the Batocera Wiki: https://wiki.batocera.org
- Moon Spot specific issues: Create an issue in this repository
