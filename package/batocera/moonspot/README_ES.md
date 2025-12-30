# Moon Spot - Kiosco Arcade Batocera con Marca Personalizada

Moon Spot es una versión con marca personalizada de Batocera Linux diseñada para instalaciones de kiosco arcade con rotación mensual de ROM, seguimiento de puntuaciones altas y soporte de señalización digital.

## Características

### 🎮 Modo Kiosco
- **Configuración bloqueada** - Previene que los usuarios modifiquen la configuración del sistema
- **Menú simplificado** - Menú estilo bartop con opciones mínimas
- **Protección automática** - La configuración se restaura si es manipulada
- **Acceso seguro** - SSH y Samba deshabilitados por defecto

### 🎯 Rotación Mensual de ROM
- **Gestión backend** - Carga y activación de ROM basada en web
- **Programación automática** - Las ROMs pueden rotarse mensualmente
- **Control de versiones** - Múltiples conjuntos de ROM pueden almacenarse y activarse
- **Despliegue fácil** - Subir paquetes tar.gz vía interfaz web

### 🏆 Seguimiento de Puntuaciones Altas
- **Integración con RetroAchievements** - Seguimiento de puntuaciones a través de múltiples juegos
- **Tablas de clasificación** - Competir por las mejores puntuaciones
- **Notificaciones de logros** - Retroalimentación visual por logros
- **Gestión centralizada** - Configurar vía interfaz web

### 📺 Señalización Digital
- **Soporte de segunda pantalla** - Mostrar contenido promocional en monitores adicionales
- **Rotación de medios** - Ciclar automáticamente a través de videos e imágenes
- **Aceleración por hardware** - Reproducción suave usando GPU
- **Gestión fácil de contenido** - Agregar/eliminar medios vía API o línea de comandos

### 🎨 Marca Personalizada
- **Pantallas de inicio personalizadas** - Animación de arranque con marca Moon Spot
- **Interfaz temática** - Apariencia personalizada de EmulationStation
- **Integración de logo** - Marca Moon Spot en todo el sistema

### 🔧 Gestión Backend
- **Interfaz web** - Panel de administración para toda la configuración
- **REST API** - Control programático de todas las características
- **Gestión remota** - Configurar desde cualquier dispositivo en la red
- **Control del sistema** - Capacidades de reinicio/apagado

## Estructura de Directorios

```
package/batocera/moonspot/
├── Config.in                       # Configuración del menú de paquetes
├── moonspot-splash/                # Pantalla de inicio y marca
│   ├── images/                     # Imágenes de logo
│   ├── videos/                     # Videos de arranque y salvapantallas
│   └── moonspot-splash.mk
├── moonspot-kiosk/                 # Modo kiosco y gestión de ROM
│   ├── scripts/
│   │   ├── moonspot-kiosk-init     # Inicialización de kiosco
│   │   ├── moonspot-settings-guard # Protección de configuración
│   │   └── moonspot-rom-manager    # Gestor de rotación de ROM
│   └── moonspot-kiosk.mk
├── moonspot-backend/               # API backend y UI web
│   ├── api/
│   │   └── moonspot-api.py         # API REST Flask
│   ├── web/
│   │   └── index.html              # Interfaz web de administración
│   └── moonspot-backend.mk
└── moonspot-signage/               # Señalización digital
    ├── scripts/
    │   ├── moonspot-signage        # Script de control de señalización
    │   └── S96moonspot-signage     # Script init
    └── moonspot-signage.mk
```

## Instalación

### Construyendo Imagen Moon Spot

1. **Clonar el repositorio** (ya hecho)

2. **Configurar la compilación:**
   ```bash
   cd batocera.linux
   make batocera-moonspot-x86_64-config
   ```

3. **Compilar la imagen:**
   ```bash
   make
   ```

4. **Grabar en tarjeta USB/SD:**
   ```bash
   dd if=output/images/batocera/batocera-moonspot-x86_64-XXXXX-XXXXXX.img of=/dev/sdX bs=4M
   ```

### Agregando Marca Personalizada

Colocar tus recursos de marca Moon Spot:

**Imágenes de Inicio:**
- `package/batocera/moonspot/moonspot-splash/images/logo.png`
- `package/batocera/moonspot/moonspot-splash/images/logo-480p.png`

**Video de Inicio:**
- `package/batocera/moonspot/moonspot-splash/videos/splash.mp4`

**Videos de Salvapantallas:**
- `package/batocera/moonspot/moonspot-splash/videos/screensaver/*.mp4`

## Configuración

### Configuración Inicial

1. **Arrancar el sistema Moon Spot**

2. **Acceder al panel de administración:**
   - Navegar a `http://moonspot:8080` o `http://<dirección-ip>:8080`
   - Credenciales por defecto: ninguna (solo acceso local)

3. **Configurar RetroAchievements:**
   - Ingresar tu nombre de usuario y contraseña de RetroAchievements
   - Habilitar seguimiento de puntuaciones altas

4. **Subir ROMs:**
   - Seleccionar el mes actual
   - Subir un paquete de ROM (.tar.gz)
   - Activar el conjunto de ROM

5. **Configurar Señalización Digital:**
   - Agregar videos/imágenes promocionales
   - Establecer intervalos de rotación
   - Habilitar en segunda pantalla

### Estructura de Paquete de ROM

Crear paquetes de ROM en este formato:

```
roms-2025-01.tar.gz
├── manifest.json
├── snes/
│   ├── juego1.smc
│   ├── juego2.smc
│   └── gamelist.xml
├── genesis/
│   ├── juego1.md
│   ├── juego2.md
│   └── gamelist.xml
└── arcade/
    ├── juego1.zip
    ├── juego2.zip
    └── gamelist.xml
```

**Ejemplo de manifest.json:**
```json
{
  "month": "2025-01",
  "name": "Colección Enero 2025",
  "systems": {
    "snes": ["juego1.smc", "juego2.smc"],
    "genesis": ["juego1.md", "juego2.md"],
    "arcade": ["juego1.zip", "juego2.zip"]
  }
}
```

## Uso

### Gestión de ROM

**Vía Interfaz Web:**
1. Abrir panel de administración: `http://moonspot:8080`
2. Seleccionar mes en la sección de Gestión de ROM
3. Subir paquete de ROM
4. Clic en "Activate Selected Month" (Activar mes seleccionado)

**Vía Línea de Comandos:**
```bash
# Descargar conjunto de ROM para el mes actual
moonspot-rom-manager download

# Activar un mes específico
moonspot-rom-manager activate 2025-01

# Listar conjuntos de ROM disponibles
moonspot-rom-manager list
```

### Señalización Digital

**Agregar medios:**
```bash
moonspot-signage add /ruta/a/video.mp4
```

**Listar medios:**
```bash
moonspot-signage list
```

**Iniciar/detener señalización:**
```bash
moonspot-signage start
moonspot-signage stop
```

### Modo Kiosco

El modo kiosco está habilitado por defecto. Para deshabilitar temporalmente para mantenimiento:

```bash
# Remover protección de configuración
chattr -i /userdata/system/batocera.conf

# Hacer cambios...

# Re-habilitar protección
chattr +i /userdata/system/batocera.conf
```

O usar la interfaz web para alternar modo kiosco.

## Referencia de API

### URL Base
`http://moonspot:8080/api`

### Endpoints

**Configuración**
- `GET /config` - Obtener configuración actual
- `POST /config` - Actualizar configuración

**Gestión de ROM**
- `GET /roms/month/<month_id>` - Obtener lista de ROM para mes
- `POST /roms/upload` - Subir paquete de ROM
- `GET /roms/download/<month_id>` - Descargar paquete de ROM
- `POST /roms/activate/<month_id>` - Activar conjunto de ROM

**Configuración de Kiosco**
- `GET /settings/kiosk` - Obtener estado de kiosco
- `POST /settings/kiosk` - Actualizar configuración de kiosco

**RetroAchievements**
- `GET /achievements/config` - Obtener configuración de logros
- `POST /achievements/config` - Actualizar configuración de logros

**Control del Sistema**
- `POST /system/reboot` - Reiniciar sistema
- `POST /system/shutdown` - Apagar sistema

## Solución de Problemas

### Las ROMs no aparecen
1. Revisar que la estructura del paquete de ROM coincida con el formato esperado
2. Verificar que manifest.json sea válido
3. Revisar registros de EmulationStation: `/userdata/system/logs/es_log.txt`

### Señalización no se muestra
1. Verificar que la segunda pantalla esté conectada y detectada:
   ```bash
   moonspot-signage detect
   ```
2. Revisar que los archivos de medios estén en el directorio correcto:
   ```bash
   moonspot-signage list
   ```
3. Verificar configuración de pantalla en `/userdata/system/moonspot/signage.conf`

### Interfaz web no accesible
1. Revisar que el servicio backend esté corriendo:
   ```bash
   /etc/init.d/S95moonspot-backend status
   ```
2. Reiniciar backend:
   ```bash
   /etc/init.d/S95moonspot-backend restart
   ```
3. Revisar configuración de firewall

### La configuración se reinicia
Este es el comportamiento esperado en modo kiosco. Para hacer cambios permanentes:
1. Acceder a la interfaz web
2. Deshabilitar modo kiosco temporalmente
3. Hacer cambios
4. Actualizar configuración maestra:
   ```bash
   moonspot-settings-guard update-master
   ```
5. Re-habilitar modo kiosco

## Créditos

Moon Spot está construido sobre [Batocera Linux](https://batocera.org), una distribución de código abierto para juegos retro.

**Arte:** Basado en la marca Moon Spot proporcionada (logo de cohete y mascota robot)

**Tecnologías:**
- Batocera Linux
- EmulationStation
- RetroArch
- Python Flask
- Reproductor de Medios MPV

## Licencia

Las personalizaciones de Moon Spot se proporcionan tal cual. Batocera Linux y sus componentes conservan sus licencias originales.

## Soporte

Para problemas y preguntas:
- Consultar la Wiki de Batocera: https://wiki.batocera.org
- Problemas específicos de Moon Spot: Crear un issue en este repositorio
