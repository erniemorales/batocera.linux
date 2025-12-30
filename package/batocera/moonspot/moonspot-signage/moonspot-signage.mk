################################################################################
#
# moonspot-signage
#
################################################################################

MOONSPOT_SIGNAGE_VERSION = 1.0
MOONSPOT_SIGNAGE_SOURCE=
MOONSPOT_SIGNAGE_DEPENDENCIES = mpv

define MOONSPOT_SIGNAGE_INSTALL_TARGET_CMDS
	# Install signage scripts
	install -m 0755 -D $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-signage/scripts/moonspot-signage \
		$(TARGET_DIR)/usr/bin/moonspot-signage

	# Install init script
	install -m 0755 -D $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-signage/scripts/S96moonspot-signage \
		$(TARGET_DIR)/etc/init.d/S96moonspot-signage

	# Create signage content directory
	mkdir -p $(TARGET_DIR)/usr/share/moonspot/signage
endef

$(eval $(generic-package))
