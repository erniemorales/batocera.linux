# Moon Spot - Guía de Inicio Rápido

## 🚀 ¿Qué es Moon Spot?

Moon Spot es una versión personalizada de Batocera Linux diseñada para instalaciones de kiosco arcade. Incluye:

- **Modo Kiosco** - Configuración bloqueada para prevenir manipulación del usuario
- **Rotación Mensual de ROMs** - Gestión fácil de ROMs con colecciones mensuales de juegos
- **Seguimiento de Puntuaciones Altas** - Integración con RetroAchievements para tablas de clasificación
- **Señalización Digital** - Muestra contenido promocional en una segunda pantalla
- **Panel de Administración Web** - Gestiona todo desde un navegador
- **✅ Soporte para Mac** - Compatible con Macs Intel, incluyendo modelos antiguos

## 💻 Compatibilidad con Mac

Moon Spot funciona en Macs Intel, incluyendo modelos antiguos como el **MacBook Pro A1226 (2007)**.

**Para usuarios de Mac:** Ver `MAC_QUICKSTART_ES.md` para instrucciones específicas de instalación y optimización.

**Modelos compatibles:**
- ✅ MacBook Pro (2007-2020)
- ✅ iMac (2007-2020)
- ✅ Mac Mini (2012-2020)
- ⚠️ Modelos con NVIDIA antigua usan driver Nouveau (suficiente para juegos retro)

## 🎮 Construyendo tu Primera Imagen Moon Spot

### Requisitos Previos

- Máquina de compilación Linux (Ubuntu 20.04+ recomendado)
- Al menos 50GB de espacio libre en disco
- 8GB+ RAM
- Buena conexión a internet

### Paso 1: Configurar la Compilación

```bash
cd batocera.linux

# Configurar para x86_64 (PC)
make batocera-moonspot-x86_64-config

# O configurar manualmente
make menuconfig
# Navegar a: System -> Moon Spot Packages -> Habilitar todos
```

### Paso 2: Agregar tu Marca

Antes de compilar, agrega tus recursos de marca Moon Spot:

```bash
# Copia tu logo (PNG 1920x1080)
cp /ruta/a/tu/logo.png \
   package/batocera/moonspot/moonspot-splash/images/logo.png

# Copia tu video de inicio (manténlo corto, <10 segundos)
cp /ruta/a/tu/splash.mp4 \
   package/batocera/moonspot/moonspot-splash/videos/splash.mp4

# Agregar contenido para el salvapantallas
mkdir -p package/batocera/moonspot/moonspot-splash/videos/screensaver
cp /ruta/a/tus/promos/*.mp4 \
   package/batocera/moonspot/moonspot-splash/videos/screensaver/
```

### Paso 3: Compilar

```bash
# Iniciar la compilación (tomará 1-2 horas)
make

# La imagen se creará en:
# output/images/batocera/batocera-*.img
```

### Paso 4: Grabar en USB/SD

**En Linux:**
```bash
# Encuentra tu dispositivo (ej., /dev/sdb)
lsblk

# Graba la imagen
sudo dd if=output/images/batocera/batocera-*.img \
        of=/dev/sdX \
        bs=4M \
        status=progress

# Sincronizar y expulsar
sync
```

**En macOS:**
```bash
# Encontrar unidad USB
diskutil list

# Desmontar
diskutil unmountDisk /dev/diskX

# Grabar imagen
sudo dd if=batocera-moonspot-x86_64-*.img \
        of=/dev/rdiskX \
        bs=4m

# Expulsar
diskutil eject /dev/diskX
```

## 📦 Preparando Paquetes de ROM

### Crear Estructura de Paquete de ROM

```bash
mkdir -p roms-2025-01/{snes,genesis,arcade}

# Copiar ROMs
cp *.smc roms-2025-01/snes/
cp *.md roms-2025-01/genesis/
cp *.zip roms-2025-01/arcade/

# Crear manifiesto
cat > roms-2025-01/manifest.json << EOF
{
  "month": "2025-01",
  "name": "Enero 2025 - Colección Clásica",
  "description": "Mejores juegos de los 90s",
  "systems": {
    "snes": ["juego1.smc", "juego2.smc"],
    "genesis": ["sonic.md", "streets-of-rage.md"],
    "arcade": ["pacman.zip", "galaga.zip"]
  }
}
EOF

# Crear paquete
tar -czf roms-2025-01.tar.gz -C roms-2025-01 .
```

## 🖥️ Configuración Inicial del Sistema

### Primer Arranque

1. **Arrancar desde USB/tarjeta SD**
2. **Esperar la pantalla de inicio de Moon Spot**
3. **Anotar la dirección IP** mostrada al arrancar

### Acceder al Panel de Administración

1. **Abrir navegador:** `http://<ip-moonspot>:8080`
2. **Configurar RetroAchievements:**
   - Usuario: Tu nombre de usuario de retroachievements.org
   - Contraseña: Tu contraseña
   - Habilitar: ✓

3. **Subir Paquete de ROM:**
   - Clic en "Choose File" (Elegir archivo)
   - Seleccionar `roms-2025-01.tar.gz`
   - Clic en "Activate Selected Month" (Activar mes seleccionado)

4. **Configurar Señalización Digital (si usas segunda pantalla):**
   - Subir videos/imágenes promocionales
   - Establecer intervalos de rotación
   - Habilitar señalización

### Habilitar Modo Kiosco

El modo kiosco está **habilitado por defecto**. La configuración está bloqueada para prevenir cambios del usuario.

Para hacer cambios:
1. Deshabilitar modo kiosco en el panel de administración
2. Hacer tus cambios
3. Re-habilitar modo kiosco

## 🏆 Configuración de RetroAchievements

### Obtener Cuenta

1. Crear cuenta en: https://retroachievements.org
2. Anotar tu nombre de usuario y contraseña

### Configurar en Moon Spot

**Vía Interfaz Web:**
1. Abrir panel de administración
2. Navegar a "High Score Tracking" (Seguimiento de Puntuación Alta)
3. Ingresar credenciales
4. Guardar

**Vía SSH (si está habilitado):**
```bash
# Editar configuración de moonspot
nano /userdata/system/moonspot/moonspot.conf

# Establecer credenciales
RETROACHIEVEMENTS_USER="tu_usuario"
RETROACHIEVEMENTS_PASSWORD="tu_contraseña"

# Reiniciar servicio de kiosco
/etc/init.d/S99moonspot-kiosk restart
```

## 📺 Configuración de Señalización Digital

### Conectar Segunda Pantalla

1. **Conectar HDMI a la segunda salida**
2. **Detectar pantallas:**
   ```bash
   moonspot-signage detect
   ```

3. **Configurar pantalla:**
   ```bash
   nano /userdata/system/moonspot/signage.conf
   ```

   Establecer:
   ```bash
   MOONSPOT_SIGNAGE_DISPLAY="HDMI-2"  # o nombre de pantalla detectado
   ROTATION_INTERVAL=30
   LOOP=true
   ```

### Agregar Contenido

**Vía Línea de Comandos:**
```bash
moonspot-signage add /ruta/a/video.mp4
moonspot-signage add /ruta/a/imagen.jpg
```

**Vía Interfaz Web:**
- Próximamente: Subir vía panel de administración

### Iniciar Señalización

```bash
moonspot-signage start

# O habilitar al arrancar
nano /userdata/system/moonspot/signage.conf
# Establecer: MOONSPOT_SIGNAGE_ENABLED=1
```

## 🔄 Rotación Mensual de ROM

### Actualización Manual

1. **Crear paquete de nuevo mes** (ej., `roms-2025-02.tar.gz`)
2. **Abrir panel de administración**
3. **Seleccionar nuevo mes**
4. **Subir paquete**
5. **Clic en "Activate Selected Month" (Activar mes seleccionado)**
6. **El sistema recargará EmulationStation**

### Actualización por Línea de Comandos

```bash
# Subir paquete al sistema
scp roms-2025-02.tar.gz root@moonspot:/tmp/

# SSH al sistema
ssh root@moonspot

# Mover al directorio de ROM
mkdir -p /userdata/system/moonspot/roms/2025-02
tar -xzf /tmp/roms-2025-02.tar.gz \
    -C /userdata/system/moonspot/roms/2025-02

# Activar
moonspot-rom-manager activate 2025-02
```

## 🔧 Tareas Comunes

### Reiniciar Servicios

```bash
# Reiniciar modo kiosco
/etc/init.d/S99moonspot-kiosk restart

# Reiniciar API backend
/etc/init.d/S95moonspot-backend restart

# Reiniciar señalización digital
/etc/init.d/S96moonspot-signage restart
```

### Ver Registros

```bash
# Registros de EmulationStation
tail -f /userdata/system/logs/es_log.txt

# Registros de API backend
journalctl -u moonspot-backend -f

# Registros del sistema
dmesg | tail -50
```

### Respaldar Configuración

```bash
# Respaldar todo
tar -czf moonspot-backup-$(date +%Y%m%d).tar.gz \
    /userdata/system/moonspot \
    /userdata/system/batocera.conf

# Restaurar
tar -xzf moonspot-backup-YYYYMMDD.tar.gz -C /
```

## 📱 Acceso por Red

### Panel de Administración
- URL: `http://moonspot:8080` o `http://<ip>:8080`

### Acceso SSH (si está habilitado)
```bash
ssh root@moonspot
# Contraseña por defecto: linux
```

### Compartir Archivos (si está habilitado)
- Windows: `\\moonspot\share`
- Mac/Linux: `smb://moonspot/share`

## 🎯 Mejores Prácticas

### Selección de ROM
- Elegir 10-15 juegos por mes
- Mezclar clásicos populares con joyas ocultas
- Incluir variedad de géneros
- Probar todos los juegos antes del despliegue

### Puntuaciones Altas
- Crear temas de competencia
- Anunciar ganadores mensuales
- Mostrar mejores puntuaciones en señalización
- Reiniciar puntuaciones mensualmente para competencia justa

### Actualizaciones de Contenido
- Actualizar contenido de señalización semanalmente
- Hacer coincidir señalización con selección actual de ROM
- Incluir consejos y trucos de juegos
- Promocionar próximos eventos

### Mantenimiento
- Revisar sistema semanalmente
- Monitorear espacio en disco
- Actualizar ROMs mensualmente
- Limpiar/reiniciar sistema mensualmente

## ❓ Solución de Problemas

### Las ROMs no Aparecen
```bash
# Revisar directorio de ROM
ls -R /userdata/roms/

# Actualizar EmulationStation
killall -HUP emulationstation
```

### Señalización no Funciona
```bash
# Detectar pantallas
moonspot-signage detect

# Revisar archivos de medios
moonspot-signage list

# Reiniciar señalización
moonspot-signage restart
```

### Panel de Administración No Accesible
```bash
# Revisar estado del servicio
/etc/init.d/S95moonspot-backend status

# Reiniciar servicio
/etc/init.d/S95moonspot-backend restart

# Revisar dirección IP
ip addr show
```

### La Configuración se Sigue Reiniciando
¡Esto es normal en modo kiosco! Para hacer cambios permanentes:
```bash
# Vía web: Deshabilitar modo kiosco → Hacer cambios → Actualizar maestro → Re-habilitar

# Vía línea de comandos:
chattr -i /userdata/system/batocera.conf
# Hacer cambios
moonspot-settings-guard update-master
chattr +i /userdata/system/batocera.conf
```

## 📚 Recursos Adicionales

- **Wiki de Batocera:** https://wiki.batocera.org
- **RetroAchievements:** https://retroachievements.org
- **EmulationStation:** https://emulationstation.org
- **Documentación Completa de Moon Spot:** Ver `package/batocera/moonspot/README_ES.md`
- **Compatibilidad con Mac:** Ver `package/batocera/moonspot/MAC_COMPATIBILITY_ES.md`
- **Guía Rápida para Mac:** Ver `package/batocera/moonspot/MAC_QUICKSTART_ES.md`

## 🎉 ¡Estás Listo!

¡Tu kiosco arcade Moon Spot ahora está configurado y listo para proporcionar una increíble experiencia de juegos retro!

¡Disfruta! 🚀🎮
