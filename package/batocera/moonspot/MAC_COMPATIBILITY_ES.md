# Moon Spot - Guía de Compatibilidad con Mac

## Modelos Mac Compatibles

Moon Spot Batocera puede ejecutarse en Macs basados en Intel con arquitectura x86_64.

### ✅ Totalmente Compatibles

**Macs Intel con GPUs Modernas:**
- MacBook Pro (2012-2020) con gráficos Intel Iris/HD
- iMac (2012-2020) con gráficos Intel o AMD
- Mac Mini (2012-2020)
- Mac Pro (2013-2019)

Estos usarán drivers de código abierto de Intel o AMD con aceleración de hardware completa.

### ⚠️ Compatibles con Limitaciones

**Macs Intel Antiguos con GPUs NVIDIA:**
- **MacBook Pro A1226 (Mediados de 2007)** - GeForce 8600M GT
- MacBook Pro (2008-2012) con gráficos NVIDIA
- iMac (2007-2011) con gráficos NVIDIA

**Información del Driver:**
- Usa **driver Nouveau de código abierto** (automático)
- Aceleración 2D completa
- Aceleración 3D básica
- Perfecto para juegos retro (NES, SNES, Genesis, PS1, N64)
- Puede tener dificultades con emuladores más pesados (GameCube, PS2, Wii)

## Información Específica de MacBook Pro A1226

### Especificaciones de Hardware
- **Modelo:** 15 pulgadas, Mediados de 2007
- **CPU:** Intel Core 2 Duo 2.2GHz o 2.4GHz
- **RAM:** 2GB-4GB DDR2
- **GPU:** NVIDIA GeForce 8600M GT (128MB o 256MB)
- **Pantalla:** 1440x900 o 1680x1050
- **Arranque:** Firmware EFI

### ¿Por Qué Nouveau en Lugar de NVIDIA Propietario?

La GeForce 8600M GT es de 2007 y requiere:
- Drivers legacy NVIDIA 340.xx (último soporte en 2019)
- No compatible con kernels Linux modernos (6.x)
- **NO incluido en las versiones actuales de Batocera**

El driver Nouveau de código abierto:
- ✅ Mantenimiento activo
- ✅ Soporta kernels modernos
- ✅ Detectado y cargado automáticamente
- ✅ Suficiente para juegos retro

### Expectativas de Rendimiento

**Funcionará Excelente:**
- Consolas de 8-bit/16-bit (NES, SNES, Genesis, Game Boy)
- Juegos de arcade (MAME, FinalBurn Neo)
- PlayStation 1
- Nintendo 64
- Dreamcast
- PSP (la mayoría de juegos)

**Funcionará (Puede Necesitar Ajustes):**
- GameCube (configuración baja)
- PS2 (solo juegos ligeros)
- Nintendo DS

**No Recomendado:**
- Wii (demasiado exigente)
- Emulación de PS3
- Sistemas modernos

## Instalación en Mac

### 1. Preparar Medio de Instalación

```bash
# En otra computadora, grabar imagen Moon Spot en USB
sudo dd if=batocera-moonspot-x86_64-*.img of=/dev/diskX bs=4M
```

### 2. Arrancar desde USB

1. **Insertar unidad USB** en Mac
2. **Encender** e inmediatamente mantener presionada la tecla **Option/Alt**
3. **Seleccionar** la opción EFI Boot (unidad USB)
4. **Esperar** la pantalla de inicio de Moon Spot

### 3. Configuración del Primer Arranque

El Mac automáticamente:
1. Detectará la NVIDIA GeForce 8600M GT
2. Cargará el driver Nouveau
3. Configurará la pantalla en resolución nativa
4. Iniciará EmulationStation

**Verificar estado del driver:**
```bash
# Presionar F4 para acceder a la terminal
cat /var/log/nvidia.log

# Debería mostrar:
# "No matching card name found for ID..."
# "Failing back to the OpenSource Mesa Nouveau driver"
```

### 4. Opcional: Forzar Nouveau

Si deseas forzar explícitamente Nouveau (normalmente no es necesario):

Editar `/boot/batocera-boot.conf`:
```bash
nvidia-driver=nouveau
```

## Consideraciones Específicas de Mac

### Arranque EFI

Los Macs usan firmware EFI, no BIOS legacy:
- ✅ Moon Spot soporta arranque EFI
- ✅ Usa cargador de arranque GRUB EFI
- ✅ Compatible con Secure Boot (si está deshabilitado)

**Deshabilitar Secure Boot (si es necesario):**
1. Arrancar en Modo de Recuperación (Cmd+R)
2. Utilidades → Utilidad de Seguridad de Inicio
3. Seleccionar "Sin Seguridad"

### Compatibilidad Wi-Fi

**MacBook Pro A1226:**
- Chip Wi-Fi: Broadcom BCM4328
- ⚠️ Puede requerir firmware propietario
- Considerar usar adaptador USB Wi-Fi o Ethernet

**Verificar estado de Wi-Fi:**
```bash
lspci | grep -i network
dmesg | grep -i firmware
```

### Bluetooth

- ✅ El Bluetooth integrado debería funcionar con drivers estándar de Linux
- Perfecto para controles inalámbricos

### Webcam/Audio

- ✅ El audio integrado debería funcionar
- ⚠️ La webcam iSight puede no funcionar (no es necesaria para juegos)

## Optimización de Rendimiento

### Para MacBook Pro A1226

**Configuraciones Recomendadas:**

1. **Deshabilitar compositor** para mejor rendimiento:
   ```bash
   # En batocera.conf
   global.videomode=1440x900
   ```

2. **Usar shaders más ligeros:**
   ```bash
   global.shaderset=none
   ```

3. **Deshabilitar gráficos suaves** para píxeles perfectos:
   ```bash
   global.smooth=0
   ```

4. **Limitar servicios en segundo plano:**
   ```bash
   kodi.enabled=0
   updates.enabled=0
   ```

### Consejos Específicos por Emulador

**Para N64:**
```bash
n64.videomode=640x480
n64.emulator=mupen64plus-next
```

**Para PSX:**
```bash
psx.videomode=640x480
psx.emulator=pcsx_rearmed
```

## Solución de Problemas

### Pantalla No Funciona

**Síntoma:** Pantalla negra o sin salida de video

**Solución:**
1. Arrancar con parámetro de kernel `nomodeset`:
   ```bash
   # Editar /boot/batocera-boot.conf
   linux.args=nomodeset
   ```

2. Probar diferentes modos de video:
   ```bash
   batocera-resolution listModes
   batocera-resolution setMode "1440x900"
   ```

### Problemas de Rendimiento

**Si los juegos corren lentamente:**

1. **Verificar throttling de CPU:**
   ```bash
   cat /proc/cpuinfo | grep MHz
   ```

2. **Monitorear temperatura:**
   ```bash
   sensors
   ```

3. **Limpiar polvo** de las rejillas (los Macs de 2007 a menudo tienen acumulación de polvo)

### Nouveau No Se Carga

**Verificar estado del driver:**
```bash
lsmod | grep nouveau
dmesg | grep nouveau
```

**Forzar carga:**
```bash
modprobe nouveau
```

## Problemas Conocidos

### Específicos de MacBook Pro A1226

1. **Control de Ventiladores:**
   - Los ventiladores pueden funcionar a velocidad fija
   - Considerar `macfanctld` si es necesario

2. **Estado de Batería:**
   - Puede no mostrarse correctamente
   - No crítico para uso de juegos

3. **Control de Brillo:**
   - Las teclas de función pueden no funcionar
   - Usar control por software si es necesario

## Características de Moon Spot en Mac

Todas las características de Moon Spot funcionan en Mac:

- ✅ Modo Kiosco
- ✅ Rotación Mensual de ROM
- ✅ RetroAchievements
- ✅ Panel de Administración Web
- ⚠️ Señalización Digital (si hay segunda pantalla conectada)

## Alternativa: Macs con GPU Dedicada

Si tienes un Mac con GPU AMD o Intel dedicada:

**Modelos con Mejor Rendimiento:**
- MacBook Pro 15" (2012-2015) - Intel Iris Pro / AMD Radeon
- iMac 27" (2013-2020) - AMD Radeon
- Mac Pro (2013-2019) - AMD FirePro

Estos usarán drivers de código abierto completamente optimizados (radeon/amdgpu/i915).

## Conclusión

**¡MacBook Pro A1226 es compatible con Moon Spot!**

✅ Arrancará y funcionará
✅ El driver Nouveau proporciona rendimiento adecuado
✅ Perfecto para juegos arcade clásicos/retro
✅ Todas las características de Moon Spot soportadas
⚠️ Rendimiento 3D limitado para emuladores exigentes

Para la mejor experiencia de kiosco arcade en este hardware, enfócate en:
- Juegos de la era 8-bit/16-bit
- Títulos de arcade clásicos
- PS1 y anteriores
- Torneos de juegos de lucha
- Juegos de puzzle

¡La combinación de las características de kiosco de Moon Spot + la construcción sólida del MacBook Pro hace un excelente gabinete arcade dedicado!

## Recursos de Soporte

- [Wiki de Batocera - Hardware de PC Soportado](https://wiki.batocera.org/supported_pc_hardware)
- [Wiki del Driver Nouveau](https://nouveau.freedesktop.org/)
- [Linux en MacBook Pro](https://wiki.archlinux.org/title/MacBookPro)

---

**Nota:** Para despliegues de kiosco en producción, considera usar una PC más moderna con gráficos Intel/AMD para rendimiento óptimo. ¡El MacBook Pro A1226 funciona excelente para uso personal/casero o como prueba de concepto!
