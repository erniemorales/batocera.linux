# Moon Spot - Mac Compatibility Guide

## Supported Mac Models

Moon Spot Batocera can run on Intel-based Macs with x86_64 architecture.

### ✅ Fully Compatible

**Intel Macs with Modern GPUs:**
- MacBook Pro (2012-2020) with Intel Iris/HD Graphics
- iMac (2012-2020) with Intel or AMD graphics
- Mac Mini (2012-2020)
- Mac Pro (2013-2019)

These will use Intel or AMD open-source drivers with full hardware acceleration.

### ⚠️ Compatible with Limitations

**Older Intel Macs with NVIDIA GPUs:**
- **MacBook Pro A1226 (Mid 2007)** - GeForce 8600M GT
- MacBook Pro (2008-2012) with NVIDIA graphics
- iMac (2007-2011) with NVIDIA graphics

**Driver Information:**
- Uses **open-source Nouveau driver** (automatic)
- Full 2D acceleration
- Basic 3D acceleration
- Perfect for retro gaming (NES, SNES, Genesis, PS1, N64)
- May struggle with heavier emulators (GameCube, PS2, Wii)

## MacBook Pro A1226 Specific Information

### Hardware Specifications
- **Model:** 15-inch, Mid 2007
- **CPU:** Intel Core 2 Duo 2.2GHz or 2.4GHz
- **RAM:** 2GB-4GB DDR2
- **GPU:** NVIDIA GeForce 8600M GT (128MB or 256MB)
- **Display:** 1440x900 or 1680x1050
- **Boot:** EFI firmware

### Why Nouveau Instead of NVIDIA Proprietary?

The GeForce 8600M GT is from 2007 and requires:
- NVIDIA 340.xx legacy drivers (last supported in 2019)
- Not compatible with modern Linux kernels (6.x)
- **Not included in current Batocera builds**

The Nouveau open-source driver:
- ✅ Actively maintained
- ✅ Supports modern kernels
- ✅ Automatically detected and loaded
- ✅ Sufficient for retro gaming

### Performance Expectations

**Will Run Great:**
- 8-bit/16-bit consoles (NES, SNES, Genesis, Game Boy)
- Arcade games (MAME, FinalBurn Neo)
- PlayStation 1
- Nintendo 64
- Dreamcast
- PSP (most games)

**Will Run (May Need Tweaking):**
- GameCube (lower settings)
- PS2 (lighter games only)
- Nintendo DS

**Not Recommended:**
- Wii (too demanding)
- PS3 emulation
- Modern systems

## Installation on Mac

### 1. Prepare Installation Media

```bash
# On another computer, flash Moon Spot image to USB
sudo dd if=batocera-moonspot-x86_64-*.img of=/dev/diskX bs=4M
```

### 2. Boot from USB

1. **Insert USB drive** into Mac
2. **Power on** and immediately hold **Option/Alt** key
3. **Select** the EFI Boot option (USB drive)
4. **Wait** for Moon Spot splash screen

### 3. First Boot Configuration

The Mac will automatically:
1. Detect the NVIDIA GeForce 8600M GT
2. Load the Nouveau driver
3. Configure display at native resolution
4. Start EmulationStation

**Check driver status:**
```bash
# Press F4 to access terminal
cat /var/log/nvidia.log

# Should show:
# "No matching card name found for ID..."
# "Failing back to the OpenSource Mesa Nouveau driver"
```

### 4. Optional: Force Nouveau

If you want to explicitly force Nouveau (not usually needed):

Edit `/boot/batocera-boot.conf`:
```bash
nvidia-driver=nouveau
```

## Mac-Specific Considerations

### EFI Boot

Macs use EFI firmware, not legacy BIOS:
- ✅ Moon Spot supports EFI boot
- ✅ Uses GRUB EFI bootloader
- ✅ Secure Boot compatible (if disabled)

**Disable Secure Boot (if needed):**
1. Boot into Recovery Mode (Cmd+R)
2. Utilities → Startup Security Utility
3. Select "No Security"

### Wi-Fi Compatibility

**MacBook Pro A1226:**
- Wi-Fi chip: Broadcom BCM4328
- ⚠️ May require proprietary firmware
- Consider using USB Wi-Fi adapter or Ethernet

**Check Wi-Fi status:**
```bash
lspci | grep -i network
dmesg | grep -i firmware
```

### Bluetooth

- Built-in Bluetooth should work with standard Linux drivers
- Perfect for wireless controllers

### Webcam/Audio

- ✅ Built-in audio should work
- ⚠️ iSight webcam may not work (not needed for gaming)

## Performance Optimization

### For MacBook Pro A1226

**Recommended Settings:**

1. **Disable compositor** for better performance:
   ```bash
   # In batocera.conf
   global.videomode=1440x900
   ```

2. **Use lighter shaders:**
   ```bash
   global.shaderset=none
   ```

3. **Disable smooth graphics** for pixel-perfect:
   ```bash
   global.smooth=0
   ```

4. **Limit background services:**
   ```bash
   kodi.enabled=0
   updates.enabled=0
   ```

### Emulator-Specific Tips

**For N64:**
```bash
n64.videomode=640x480
n64.emulator=mupen64plus-next
```

**For PSX:**
```bash
psx.videomode=640x480
psx.emulator=pcsx_rearmed
```

## Troubleshooting

### Display Not Working

**Symptom:** Black screen or no video output

**Solution:**
1. Boot with `nomodeset` kernel parameter:
   ```bash
   # Edit /boot/batocera-boot.conf
   linux.args=nomodeset
   ```

2. Try different video modes:
   ```bash
   batocera-resolution listModes
   batocera-resolution setMode "1440x900"
   ```

### Performance Issues

**If games run slowly:**

1. **Check CPU throttling:**
   ```bash
   cat /proc/cpuinfo | grep MHz
   ```

2. **Monitor temperature:**
   ```bash
   sensors
   ```

3. **Clean dust** from vents (Macs from 2007 often have dust buildup)

### Nouveau Not Loading

**Check driver status:**
```bash
lsmod | grep nouveau
dmesg | grep nouveau
```

**Force load:**
```bash
modprobe nouveau
```

## Known Issues

### MacBook Pro A1226 Specific

1. **Fan Control:**
   - Fans may run at fixed speed
   - Consider `macfanctld` if needed

2. **Battery Status:**
   - May not display correctly
   - Not critical for gaming use

3. **Brightness Control:**
   - Function keys may not work
   - Use software control if needed

## Moon Spot Features on Mac

All Moon Spot features work on Mac:

- ✅ Kiosk Mode
- ✅ Monthly ROM Rotation
- ✅ RetroAchievements
- ✅ Web Admin Panel
- ⚠️ Digital Signage (if second display connected)

## Alternative: Dedicated GPU Macs

If you have a Mac with dedicated AMD or Intel GPU:

**Better Performance Models:**
- MacBook Pro 15" (2012-2015) - Intel Iris Pro / AMD Radeon
- iMac 27" (2013-2020) - AMD Radeon
- Mac Pro (2013-2019) - AMD FirePro

These will use fully optimized open-source drivers (radeon/amdgpu/i915).

## Conclusion

**MacBook Pro A1226 is compatible with Moon Spot!**

✅ Will boot and run
✅ Nouveau driver provides adequate performance
✅ Perfect for classic arcade/retro gaming
✅ All Moon Spot features supported
⚠️ Limited 3D performance for demanding emulators

For the best arcade kiosk experience on this hardware, focus on:
- 8-bit/16-bit era games
- Classic arcade titles
- PS1 and earlier
- Fighting games tournaments
- Puzzle games

The combination of Moon Spot's kiosk features + MacBook Pro's solid build quality makes for an excellent dedicated arcade cabinet!

## Support Resources

- [Batocera Wiki - Supported PC Hardware](https://wiki.batocera.org/supported_pc_hardware)
- [Nouveau Driver Wiki](https://nouveau.freedesktop.org/)
- [Linux on MacBook Pro](https://wiki.archlinux.org/title/MacBookPro)

---

**Note:** For production kiosk deployments, consider using a more modern PC with Intel/AMD graphics for optimal performance. The MacBook Pro A1226 works great for personal/home use or as a proof-of-concept!
