# Moon Spot - Guía Rápida para Mac

## Compatibilidad con MacBook Pro A1226 ✅

**¡Buenas noticias!** Tu MacBook Pro A1226 (Mediados de 2007) **ejecutará Moon Spot** usando el driver de código abierto Nouveau.

### Qué Funciona

✅ Soporte completo de pantalla (1440x900 o 1680x1050)
✅ Gráficos acelerados por hardware (driver Nouveau)
✅ Todas las características de Moon Spot (modo kiosco, rotación de ROM, RetroAchievements)
✅ Juegos retro clásicos (NES, SNES, Genesis, PS1, N64)
✅ Soporte de arranque EFI
✅ Controles inalámbricos vía Bluetooth

### Qué Esperar

⚠️ Usa **Nouveau** (código abierto) en lugar de drivers NVIDIA propietarios
⚠️ GeForce 8600M GT no soportada por drivers NVIDIA modernos
⚠️ Menor rendimiento 3D que drivers propietarios
⚠️ Emulación de GameCube/PS2 puede ser limitada

## Instalación Rápida

### 1. Descargar Imagen Moon Spot

Compila Moon Spot o descarga la imagen pre-compilada:
```bash
# Compilar tú mismo
make batocera-moonspot-x86_64-config
make
```

### 2. Grabar en Unidad USB

**En macOS:**
```bash
# Encontrar tu unidad USB
diskutil list

# Desmontar (reemplazar diskX con tu unidad)
diskutil unmountDisk /dev/diskX

# Grabar imagen (¡ESTO BORRARÁ LA UNIDAD USB!)
sudo dd if=batocera-moonspot-x86_64-*.img of=/dev/rdiskX bs=4m
```

**En Linux:**
```bash
sudo dd if=batocera-moonspot-x86_64-*.img of=/dev/sdX bs=4M status=progress
```

### 3. Arrancar MacBook Pro desde USB

1. **Insertar unidad USB**
2. **Encender** Mac
3. **Mantener presionada inmediatamente** la tecla **Option/Alt**
4. **Seleccionar** "EFI Boot" o "Unidad USB"
5. **Esperar** pantalla de inicio de Moon Spot

### 4. Primer Arranque

El sistema:
1. ✅ Detectará GeForce 8600M GT
2. ✅ Cargará automáticamente driver Nouveau
3. ✅ Configurará resolución nativa de pantalla
4. ✅ Iniciará EmulationStation con marca Moon Spot

## Verificar Estado del Driver

Presionar **F4** para acceder a la terminal:

```bash
# Revisar log del driver
cat /var/log/nvidia.log

# Debería mostrar:
# "No matching card name found for ID..."
# "Failing back to the OpenSource Mesa Nouveau driver"

# Verificar que Nouveau está cargado
lsmod | grep nouveau

# Revisar información de gráficos
glxinfo | grep renderer
```

## Optimización para MacBook Pro A1226

### Configuración Recomendada de batocera.conf

Copiar la configuración optimizada para Mac:
```bash
cp /userdata/system/batocera.conf.mac /userdata/system/batocera.conf
```

**Optimizaciones clave:**
```bash
# Deshabilitar shaders para mejor rendimiento
global.shaderset=none

# Gráficos con píxeles perfectos
global.smooth=0

# Deshabilitar características intensivas de CPU
global.rewind=0
global.autosave=0

# Deshabilitar Kodi
kodi.enabled=0
```

### Emuladores con Mejor Rendimiento

**Rendimiento Excelente:**
- NES / Famicom
- SNES / Super Famicom
- Sega Genesis / Mega Drive
- Game Boy / Game Boy Color / Game Boy Advance
- Arcade (MAME, FinalBurn Neo)
- PlayStation 1
- Nintendo 64 (mayoría de juegos)
- Dreamcast (mayoría de juegos)

**Buen Rendimiento (puede necesitar ajustes):**
- PSP (juegos ligeros)
- Nintendo DS
- Dreamcast (juegos exigentes)

**Rendimiento Limitado:**
- GameCube (solo configuración baja)
- PlayStation 2 (muy limitado)
- Wii (no recomendado)

## Configurar Características de Moon Spot

### 1. Acceder al Panel de Administración Web

Después del arranque, anotar la dirección IP mostrada en pantalla:
```
http://<dirección-ip>:8080
```

O encontrarla:
```bash
# Desde terminal (F4)
ip addr show | grep inet
```

### 2. Configurar RetroAchievements

1. Abrir panel web
2. Navegar a "High Score Tracking" (Seguimiento de Puntuación Alta)
3. Ingresar tus credenciales de retroachievements.org
4. Guardar

### 3. Subir Paquetes de ROM

Crear un paquete de ROM para el mes:
```bash
# Estructura de ejemplo
roms-2025-01/
├── manifest.json
├── snes/
├── genesis/
└── arcade/

# Empaquetar
tar -czf roms-2025-01.tar.gz -C roms-2025-01 .
```

Subir vía interfaz web o copiar a:
```bash
/userdata/system/moonspot/roms/2025-01/
```

Activar:
```bash
moonspot-rom-manager activate 2025-01
```

### 4. Agregar Contenido de Salvapantallas

```bash
# Copiar videos promocionales
moonspot-signage add /ruta/a/video-promo.mp4

# O copiar directamente
cp videos/*.mp4 /usr/share/moonspot/screensaver/
```

## Solución de Problemas

### Pantalla Negra al Arrancar

**Probar modo gráfico seguro:**
1. En menú GRUB, presionar 'e'
2. Agregar `nomodeset` a línea linux
3. Presionar Ctrl+X para arrancar

**O editar configuración de arranque:**
```bash
# Montar partición de arranque
mount /dev/sda1 /boot

# Editar configuración
nano /boot/batocera-boot.conf

# Agregar:
linux.args=nomodeset
```

### Resolución de Pantalla Incorrecta

```bash
# Listar modos disponibles
batocera-resolution listModes

# Establecer modo correcto
batocera-resolution setMode "1440x900"

# Hacer permanente en batocera.conf
echo "global.videomode=1440x900" >> /userdata/system/batocera.conf
```

### Problemas de Rendimiento

**Verificar frecuencia de CPU:**
```bash
cat /proc/cpuinfo | grep MHz
```

**Monitorear temperatura:**
```bash
sensors
```

**¡Limpiar polvo de las rejillas!** (Los MacBooks de 2007 a menudo tienen acumulación de polvo)

### Wi-Fi No Funciona

MacBook Pro A1226 usa Broadcom BCM4328:
```bash
# Verificar si está detectado
lspci | grep Network

# Verificar estado del firmware
dmesg | grep firmware
```

**Solución alternativa:** Usar adaptador USB Wi-Fi o Ethernet

## Consejos de Rendimiento

### 1. Cerrar Aplicaciones en Segundo Plano
```bash
# Detener servicios innecesarios
/etc/init.d/S95moonspot-backend stop  # Si no usas admin web
```

### 2. Reducir Configuraciones de EmulationStation
```bash
# Deshabilitar transiciones
system.es.transitions=instant

# Reducir calidad de salvapantallas
system.es.screensaver.time=300000
```

### 3. Ajustes por Emulador

**Para N64:**
```bash
n64.videomode=640x480
n64.core=mupen64plus-next
n64.frameskip=1  # Si es necesario
```

**Para PSX:**
```bash
psx.videomode=640x480
psx.core=pcsx_rearmed
```

### 4. Deshabilitar Efectos Visuales
```bash
# En configuración de UI de EmulationStation:
- Establecer Tema a simple/carbon
- Deshabilitar vistas previas de video en lista de juegos
- Reducir animaciones de transición
```

## Características Específicas de Mac

### Controles Bluetooth

Funciona excelente con:
- Controles PS3
- Controles PS4
- Controles Xbox
- Controles 8BitDo

**Emparejar vía EmulationStation:**
1. Menú Principal → Controles
2. Emparejar control Bluetooth
3. Seguir instrucciones en pantalla

### Configuración Multi-Pantalla

Si conectas monitor externo:
```bash
# Detectar pantallas
xrandr

# Configurar pantallas duales
xrandr --output LVDS-1 --auto --output HDMI-1 --auto --right-of LVDS-1
```

## Casos de Uso Recomendados

### Perfecto Para:
✅ Gabinete arcade casero usando MacBook antiguo
✅ Estación de juegos retro portátil
✅ Torneos de juegos de lucha (SF2, KOF, etc.)
✅ Competencias de arcade clásicos
✅ Juegos de fiesta (Mario Kart 64, GoldenEye, etc.)

### No Ideal Para:
❌ Emulación moderna (PS3, Switch, etc.)
❌ Juegos intensivos en gráficos
❌ Kiosco de producción que necesita máximo rendimiento

## Próximos Pasos

1. **Agregar tu marca Moon Spot:**
   - Logo: `/package/batocera/moonspot/moonspot-splash/images/logo.png`
   - Videos: `/package/batocera/moonspot/moonspot-splash/videos/`

2. **Crear paquetes de ROM** para rotación mensual

3. **Probar emuladores** para encontrar cores con mejor rendimiento

4. **Configurar RetroAchievements** para seguimiento de puntuaciones altas

5. **Configurar modo kiosco** para despliegue público

## Documentación Completa

- **Compatibilidad Detallada con Mac:** `MAC_COMPATIBILITY_ES.md`
- **Características de Moon Spot:** `README_ES.md`
- **Guía Rápida General:** `MOONSPOT_QUICKSTART_ES.md`

## Soporte

Para problemas específicos de Moon Spot:
- GitHub: Crear un issue

Para soporte general de Batocera:
- Wiki: https://wiki.batocera.org
- Foro: https://forum.batocera.org

---

**¡Disfruta tu arcade Moon Spot con Mac! 🚀🎮**
