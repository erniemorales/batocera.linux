# Moon Spot - Mac Quick Start Guide

## MacBook Pro A1226 Compatibility ✅

**Good news!** Your MacBook Pro A1226 (Mid 2007) **will run Moon Spot** using the open-source Nouveau driver.

### What Works

✅ Full display support (1440x900 or 1680x1050)
✅ Hardware-accelerated graphics (Nouveau driver)
✅ All Moon Spot features (kiosk mode, ROM rotation, RetroAchievements)
✅ Classic retro gaming (NES, SNES, Genesis, PS1, N64)
✅ EFI boot support
✅ Wireless controllers via Bluetooth

### What to Expect

⚠️ Uses **Nouveau** (open-source) instead of NVIDIA proprietary drivers
⚠️ GeForce 8600M GT not supported by modern NVIDIA drivers
⚠️ Lower 3D performance than proprietary drivers
⚠️ GameCube/PS2 emulation may be limited

## Quick Installation

### 1. Download Moon Spot Image

Build Moon Spot or download the pre-built image:
```bash
# Build yourself
make batocera-moonspot-x86_64-config
make
```

### 2. Flash to USB Drive

**On macOS:**
```bash
# Find your USB drive
diskutil list

# Unmount (replace diskX with your drive)
diskutil unmountDisk /dev/diskX

# Flash image (THIS WILL ERASE THE USB DRIVE!)
sudo dd if=batocera-moonspot-x86_64-*.img of=/dev/rdiskX bs=4m
```

**On Linux:**
```bash
sudo dd if=batocera-moonspot-x86_64-*.img of=/dev/sdX bs=4M status=progress
```

### 3. Boot MacBook Pro from USB

1. **Insert USB drive**
2. **Power on** Mac
3. **Immediately hold** the **Option/Alt** key
4. **Select** "EFI Boot" or "USB Drive"
5. **Wait** for Moon Spot splash screen

### 4. First Boot

The system will:
1. ✅ Detect GeForce 8600M GT
2. ✅ Automatically load Nouveau driver
3. ✅ Configure native display resolution
4. ✅ Start EmulationStation with Moon Spot branding

## Verifying Driver Status

Press **F4** to access the terminal:

```bash
# Check driver log
cat /var/log/nvidia.log

# Should show:
# "No matching card name found for ID..."
# "Failing back to the OpenSource Mesa Nouveau driver"

# Verify Nouveau is loaded
lsmod | grep nouveau

# Check graphics info
glxinfo | grep renderer
```

## Optimizing for MacBook Pro A1226

### Recommended batocera.conf Settings

Copy the Mac-optimized config:
```bash
cp /userdata/system/batocera.conf.mac /userdata/system/batocera.conf
```

**Key optimizations:**
```bash
# Disable shaders for better performance
global.shaderset=none

# Pixel-perfect graphics
global.smooth=0

# Disable CPU-intensive features
global.rewind=0
global.autosave=0

# Disable Kodi
kodi.enabled=0
```

### Best Performing Emulators

**Excellent Performance:**
- NES / Famicom
- SNES / Super Famicom
- Sega Genesis / Mega Drive
- Game Boy / Game Boy Color / Game Boy Advance
- Arcade (MAME, FinalBurn Neo)
- PlayStation 1
- Nintendo 64 (most games)
- Dreamcast (most games)

**Good Performance (may need tweaking):**
- PSP (lighter games)
- Nintendo DS
- Dreamcast (demanding games)

**Limited Performance:**
- GameCube (lower settings only)
- PlayStation 2 (very limited)
- Wii (not recommended)

## Setting Up Moon Spot Features

### 1. Access Web Admin Panel

After boot, note the IP address shown on screen:
```
http://<ip-address>:8080
```

Or find it:
```bash
# From terminal (F4)
ip addr show | grep inet
```

### 2. Configure RetroAchievements

1. Open web panel
2. Navigate to "High Score Tracking"
3. Enter your retroachievements.org credentials
4. Save

### 3. Upload ROM Packages

Create a ROM package for the month:
```bash
# Example structure
roms-2025-01/
├── manifest.json
├── snes/
├── genesis/
└── arcade/

# Package it
tar -czf roms-2025-01.tar.gz -C roms-2025-01 .
```

Upload via web interface or copy to:
```bash
/userdata/system/moonspot/roms/2025-01/
```

Activate:
```bash
moonspot-rom-manager activate 2025-01
```

### 4. Add Screensaver Content

```bash
# Copy promotional videos
moonspot-signage add /path/to/promo-video.mp4

# Or copy directly
cp videos/*.mp4 /usr/share/moonspot/screensaver/
```

## Troubleshooting

### Black Screen on Boot

**Try safe graphics mode:**
1. At GRUB menu, press 'e'
2. Add `nomodeset` to linux line
3. Press Ctrl+X to boot

**Or edit boot config:**
```bash
# Mount boot partition
mount /dev/sda1 /boot

# Edit config
nano /boot/batocera-boot.conf

# Add:
linux.args=nomodeset
```

### Display Resolution Wrong

```bash
# List available modes
batocera-resolution listModes

# Set correct mode
batocera-resolution setMode "1440x900"

# Make permanent in batocera.conf
echo "global.videomode=1440x900" >> /userdata/system/batocera.conf
```

### Performance Issues

**Check CPU frequency:**
```bash
cat /proc/cpuinfo | grep MHz
```

**Monitor temperature:**
```bash
sensors
```

**Clean dust from vents!** (2007 MacBooks often have dust buildup)

### Wi-Fi Not Working

MacBook Pro A1226 uses Broadcom BCM4328:
```bash
# Check if detected
lspci | grep Network

# Check firmware status
dmesg | grep firmware
```

**Workaround:** Use USB Wi-Fi adapter or Ethernet

## Performance Tips

### 1. Close Background Apps
```bash
# Stop unnecessary services
/etc/init.d/S95moonspot-backend stop  # If not using web admin
```

### 2. Lower EmulationStation Settings
```bash
# Disable transitions
system.es.transitions=instant

# Reduce screensaver quality
system.es.screensaver.time=300000
```

### 3. Per-Emulator Tweaks

**For N64:**
```bash
n64.videomode=640x480
n64.core=mupen64plus-next
n64.frameskip=1  # If needed
```

**For PSX:**
```bash
psx.videomode=640x480
psx.core=pcsx_rearmed
```

### 4. Disable Visual Effects
```bash
# In EmulationStation UI settings:
- Set Theme to simple/carbon
- Disable video previews in gamelist
- Reduce transition animations
```

## Mac-Specific Features

### Bluetooth Controllers

Works great with:
- PS3 controllers
- PS4 controllers
- Xbox controllers
- 8BitDo controllers

**Pair via EmulationStation:**
1. Main Menu → Controllers
2. Pair Bluetooth controller
3. Follow on-screen instructions

### Multi-Display Setup

If connecting external monitor:
```bash
# Detect displays
xrandr

# Configure dual displays
xrandr --output LVDS-1 --auto --output HDMI-1 --auto --right-of LVDS-1
```

## Recommended Use Cases

### Perfect For:
✅ Home arcade cabinet using old MacBook
✅ Portable retro gaming station
✅ Fighting game tournaments (SF2, KOF, etc.)
✅ Classic arcade competitions
✅ Party gaming (Mario Kart 64, GoldenEye, etc.)

### Not Ideal For:
❌ Modern emulation (PS3, Switch, etc.)
❌ Graphics-intensive games
❌ Production kiosk needing max performance

## Next Steps

1. **Add your Moon Spot branding:**
   - Logo: `/package/batocera/moonspot/moonspot-splash/images/logo.png`
   - Videos: `/package/batocera/moonspot/moonspot-splash/videos/`

2. **Create ROM packages** for monthly rotation

3. **Test emulators** to find best-performing cores

4. **Set up RetroAchievements** for high score tracking

5. **Configure kiosk mode** for public deployment

## Full Documentation

- **Detailed Mac Compatibility:** `MAC_COMPATIBILITY.md`
- **Moon Spot Features:** `README.md`
- **General Quick Start:** `MOONSPOT_QUICKSTART.md`

## Support

For Moon Spot specific issues:
- GitHub: Create an issue

For Batocera general support:
- Wiki: https://wiki.batocera.org
- Forum: https://forum.batocera.org

---

**Enjoy your Mac-powered Moon Spot arcade! 🚀🎮**
