################################################################################
#
# moonspot-backend
#
################################################################################

MOONSPOT_BACKEND_VERSION = 1.0
MOONSPOT_BACKEND_SOURCE=
MOONSPOT_BACKEND_DEPENDENCIES = python3 python-flask python-flask-cors

define MOONSPOT_BACKEND_INSTALL_TARGET_CMDS
	# Install backend API
	mkdir -p $(TARGET_DIR)/usr/share/moonspot/backend
	cp -r $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-backend/api/* \
		$(TARGET_DIR)/usr/share/moonspot/backend/

	# Install web interface
	mkdir -p $(TARGET_DIR)/usr/share/moonspot/web
	cp -r $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-backend/web/* \
		$(TARGET_DIR)/usr/share/moonspot/web/

	# Install systemd service
	install -m 0755 -D $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/moonspot/moonspot-backend/S95moonspot-backend \
		$(TARGET_DIR)/etc/init.d/S95moonspot-backend
endef

$(eval $(generic-package))
