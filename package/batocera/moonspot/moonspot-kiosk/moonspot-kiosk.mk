################################################################################
#
# moonspot-kiosk
#
################################################################################

MOONSPOT_KIOSK_VERSION = 1.0
MOONSPOT_KIOSK_SOURCE=

define MOONSPOT_KIOSK_INSTALL_TARGET_CMDS
	# Install kiosk mode configuration script
	install -m 0755 -D $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-kiosk/scripts/moonspot-kiosk-init \
		$(TARGET_DIR)/etc/init.d/S99moonspot-kiosk

	# Install settings protection script
	install -m 0755 -D $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-kiosk/scripts/moonspot-settings-guard \
		$(TARGET_DIR)/usr/bin/moonspot-settings-guard

	# Install ROM rotation manager
	install -m 0755 -D $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-kiosk/scripts/moonspot-rom-manager \
		$(TARGET_DIR)/usr/bin/moonspot-rom-manager
endef

$(eval $(generic-package))
