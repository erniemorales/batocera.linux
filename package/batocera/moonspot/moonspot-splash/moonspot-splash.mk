################################################################################
#
# moonspot-splash
#
################################################################################

MOONSPOT_SPLASH_VERSION = 1.0
MOONSPOT_SPLASH_SOURCE=

# Install Moon Spot branded splash screens
define MOONSPOT_SPLASH_INSTALL_TARGET_CMDS
	mkdir -p $(TARGET_DIR)/usr/share/batocera/splash
	mkdir -p $(TARGET_DIR)/usr/share/moonspot

	# Install splash video/images
	if [ -f $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-splash/videos/splash.mp4 ]; then \
		cp $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-splash/videos/splash.mp4 \
		   $(TARGET_DIR)/usr/share/batocera/splash/splash.mp4; \
	fi

	# Install boot logo
	if [ -f $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-splash/images/logo.png ]; then \
		cp $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-splash/images/logo.png \
		   $(TARGET_DIR)/usr/share/batocera/splash/boot-logo.png; \
	fi

	# Install screensaver videos
	if [ -d $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-splash/videos/screensaver ]; then \
		mkdir -p $(TARGET_DIR)/usr/share/moonspot/screensaver; \
		cp -r $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-splash/videos/screensaver/* \
		   $(TARGET_DIR)/usr/share/moonspot/screensaver/; \
	fi
endef

$(eval $(generic-package))
