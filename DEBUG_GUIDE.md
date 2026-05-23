# 🔧 DEBUG GUIDE - HIBRID CIBERSEGURIDAD

## 📋 Resumen de Cambios

### ❌ **Problemas Identificados**

#### 1. **aggressive_siege_test.py - CRÍTICO**
- ❌ 10,000,000 de ataques simultáneos
- ❌ 2,000 workers agotando RAM
- ❌ Sin monitoreo de recursos
- ❌ Riesgo de crash del sistema
- ❌ Payloads de DDoS real (riesgo legal)

#### 2. **Sin Herramienta de Diagnóstico**
- ❌ No hay forma de validar el entorno
- ❌ No se verifica Python 3.8+
- ❌ No se validan dependencias

#### 3. **Sin Límites de Sistema**
- ❌ CPU: sin límites
- ❌ RAM: sin límites
- ❌ Sin pausas automáticas

---

## ✅ **Soluciones Implementadas**

### 1. **stress_test.py** - Test Inteligente
```bash
Características:
✅ 5,000 ataques (configurable)
✅ Auto-detección de CPUs
✅ Monitoreo CPU/RAM en tiempo real
✅ Pausas automáticas si > 85% CPU
✅ Pausas automáticas si > 80% RAM
✅ 4 tipos de pruebas adaptativas
✅ Logging a archivo + consola
✅ Reporte JSON detallado
✅ Hash de integridad en registros
```

### 2. **system_debugger.py** - Diagnóstico Completo
```bash
Verifica:
✅ Python 3.8+ (REQUERIDO)
✅ 16+ dependencias instaladas
✅ 10 puertos monitoreados
✅ CPU/RAM/Disco en vivo
✅ Conectividad de red
✅ Base de datos SQLite
✅ Archivos necesarios
✅ Permisos de archivo
✅ Genera reporte JSON
```

### 3. **requirements.txt** - Dependencias Actualizadas
```bash
✅ Versiones seguras y compatibles
✅ Comentarios por sección
✅ Sin conflictos de dependencias
```

---

## 🚀 **Guía de Uso**

### Paso 1: Diagnosticar Sistema
```bash
python system_debugger.py
```

**Salida esperada:**
```
✅ Python: 3.9.0 (linux)
✅ Dependencias: 16/16 (100%)
✅ CPU: 4 cores | Uso: 45.2%
✅ RAM: 8.00GB | Usado: 4.25GB (53.1%)
✅ DISCO: 100.00GB | Usado: 45.50GB (45.5%)
✅ RED: ✅ ONLINE
```

### Paso 2: Instalar Dependencias (si falta algo)
```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar Test Pequeño
```bash
# 1,000 pruebas
python stress_test.py --attacks 1000
```

### Paso 4: Ejecutar Test Estándar
```bash
# 5,000 pruebas (default)
python stress_test.py
```

### Paso 5: Ejecutar Test Personalizado
```bash
# 10,000 pruebas con 30 workers
python stress_test.py --attacks 10000 --workers 30
```

### Paso 6: Revisar Resultados
```bash
# Ver último reporte de stress test
cat stress_test_results_*.json | tail -1

# Ver último reporte de diagnóstico
cat debug_report_*.json | tail -1

# Ver logs
tail -f stress_test.log
```

---

## 📊 **Comparativa Antes vs Después**

| Aspecto | ANTES ❌ | DESPUÉS ✅ |
|--------|---------|----------|
| **Ataques** | 10,000,000 | 5,000 |
| **Workers** | 2,000 | CPU*2 (max 50) |
| **Monitoreo CPU** | ❌ | ✅ En vivo |
| **Límite CPU** | ❌ | ✅ 85% |
| **Límite RAM** | ❌ | ✅ 80% |
| **Pausas** | ❌ | ✅ Automáticas |
| **Diagnosticar** | ❌ | ✅ Completo |
| **Crash Riesgo** | 💥 Alto | ✅ Bajo |
| **Payloads** | 🔴 Real | 🟢 Educativo |

---

## 🎯 **Troubleshooting**

### Problema: "ModuleNotFoundError: No module named 'flask'"
```bash
# Solución:
pip install -r requirements.txt
python system_debugger.py  # Verifica
```

### Problema: "Permission denied" en stress_test.py
```bash
# Solución:
chmod +x stress_test.py
chmod +x system_debugger.py
```

### Problema: "Port already in use"
```bash
# Ver qué proceso usa el puerto:
lsof -i :5000
# Matar proceso:
kill -9 <PID>
```

### Problema: RAM muy alta después de test
```bash
# Normal - se libera automáticamente
# Si persiste:
python system_debugger.py  # Verifica recursos
# Reinicia el sistema si es necesario
```

### Problema: CPU al 100% durante test
```bash
# Normal durante stress_test
# Se pausa automáticamente cuando > 85%
# Puedes interrumpir con: Ctrl+C
```

---

## 📈 **Salida Esperada - stress_test.py**

```
⚡ STRESS TEST OPTIMIZADO - HIBRID SECURITY ⚡

Target: 127.0.0.1
Total Pruebas: 5,000
Workers: 8
CPU Límite: 85% | RAM Límite: 80%
Inicio: 2026-05-23 10:30:31

[500/5,000] ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 10.0% | 
Velocidad: 1,234 pruebas/seg | CPU: 45.2% | RAM: 62.3% | ETA: 3s

[1,000/5,000] ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 20.0% | 
Velocidad: 1,205 pruebas/seg | CPU: 52.1% | RAM: 65.8% | ETA: 3s

...

📊 RESULTADOS DEL TEST 📊

✅ Exitosas:          3,250
⛔ Bloqueadas:        2,100
🔓 Puertos Abiertos:  2,850
🔒 Puertos Cerrados:  1,800
❌ Errores:             800

⏱️  Tiempo Total:      4.25s
🚀 Velocidad Promedio: 2,352 pruebas/seg
📈 Total Registros:   10,000
⏸️  Pausas del Sistema: 2
🔐 Integridad OK:     True

✅ Resultados guardados en: stress_test_results_20260523_103031.json
📋 Total de registros: 10,000
```

---

## 📝 **Salida Esperada - system_debugger.py**

```
🔍 SYSTEM DEBUGGER - HIBRID CIBERSEGURIDAD 🔍

Iniciando diagnóstico completo del sistema...

✅ Python: 3.9.0 (linux)

🔍 Verificando dependencias:
  ✅ flask
  ✅ werkzeug
  ✅ cryptography
  ... (16 dependencias total)

🖥️  Recursos del Sistema:
  ✅ CPU: 4 cores | Uso: 45.2%
  ✅ RAM: 8.00GB | Usado: 4.25GB (53.1%)
  ✅ DISCO: 100.00GB | Usado: 45.50GB (45.5%)

🌐 Puertos Monitoreados:
  22    - 🔴 CERRADO
  80    - 🔴 CERRADO
  443   - 🔴 CERRADO
  5000  - 🔴 CERRADO
  ... (10 puertos total)

💾 Base de Datos:
  ⚠️  threats.db NO encontrada (se creará en primer uso)

📁 Archivos Necesarios:
  ✅ app.py
  ✅ auth.py
  ✅ stress_test.py
  ✅ requirements.txt
  ✅ README.md
  ... (8 archivos total)

🔐 Permisos:
  ✅ app.py - R:True, W:True
  ✅ requirements.txt - R:True, W:True

📡 Red:
  ✅ Hostname: my-pc
  ✅ IP Local: 192.168.1.100
  ✅ Conectividad: ONLINE

🔧 RESUMEN DEL DIAGNÓSTICO 🔧

Python:           ✅
Dependencias:     100% instaladas
Archivos:         8/8
Base de Datos:    ⚠️
Red:              ✅ ONLINE

Estado General:   OK

✅ Reporte guardado: debug_report_20260523_103031.json

🎯 Próximos pasos:
  1. Revisar dependencias faltantes: pip install -r requirements.txt
  2. Ejecutar stress test: python stress_test.py
  3. Iniciar aplicación: python app.py
```

---

## 🔒 **Notas de Seguridad**

✅ **aggressive_siege_test.py eliminado** - Contenía payloads de DDoS real
✅ **stress_test.py educativo** - Solo pruebas de conectividad
✅ **Sin payloads maliciosos** - Cumple con ley
✅ **Monitoreo en tiempo real** - No daña el sistema
✅ **Aislado** - Solo localhost por defecto

---

## 📞 **Soporte**

Si encuentras problemas:

1. Ejecuta: `python system_debugger.py`
2. Revisa: `debug_report_*.json`
3. Busca errores en: `stress_test.log`
4. Verifica: `stress_test_results_*.json`

---

**Actualizado:** 23/05/2026  
**Versión:** 2.0 (Optimizada)  
**Estado:** ✅ Producción lista
