# Moon Spot Digital Signage

This package enables digital signage support for a second screen.

## Features

- **Automatic media rotation** - Displays videos and images in a loop
- **Multi-display support** - Automatically detects and uses second screen
- **Easy content management** - Add/remove media via command line or API
- **Hardware acceleration** - Uses GPU for smooth playback

## Configuration

Create `/userdata/system/moonspot/signage.conf`:

```bash
# Display to use (default: HDMI-2)
MOONSPOT_SIGNAGE_DISPLAY="HDMI-2"

# Rotation interval for images (seconds)
ROTATION_INTERVAL=30

# Loop media continuously
LOOP=true

# Shuffle playback
SHUFFLE=true
```

## Usage

```bash
# Start signage
moonspot-signage start

# Stop signage
moonspot-signage stop

# Add media
moonspot-signage add /path/to/video.mp4

# List media
moonspot-signage list

# Remove media
moonspot-signage remove video.mp4
```

## Media Directory

Place media files in: `/usr/share/moonspot/signage/`

Supported formats:
- Videos: .mp4, .webm
- Images: .jpg, .png

## API Integration

The backend API can manage signage content:
- `POST /api/signage/upload` - Upload media
- `GET /api/signage/list` - List media files
- `DELETE /api/signage/<filename>` - Remove media
