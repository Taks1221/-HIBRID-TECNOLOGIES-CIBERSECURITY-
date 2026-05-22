# 🔒 SISTEMA DE CIBERSEGURIDAD - Honeypot & IA

Dashboard web para gestionar amenazas de ciberseguridad con **Honeypot** y **análisis de IA**.

## ✨ Características

- 🍯 **Honeypot** - Monitorea 7 puertos comunes simultáneamente
- 🤖 **IA/ML** - Detecta y clasifica automáticamente tipos de amenazas
- 📊 **Dashboard** - Interfaz web en tiempo real
- 💾 **Base de datos** - SQLite para almacenar eventos
- ⚡ **Rápido** - Implementación simple y eficiente

## 🚀 Puertos Monitoreados

- **22** - SSH
- **23** - Telnet
- **80** - HTTP
- **443** - HTTPS
- **3306** - MySQL
- **5432** - PostgreSQL
- **27017** - MongoDB

## 📋 Requisitos

- Python 3.8+
- pip

## 💿 Instalación

```bash
# Clonar repositorio
git clone https://github.com/Taks1221/-HIBRID-TECNOLOGIES-CIBERSECURITY-.git
cd -HIBRID-TECNOLOGIES-CIBERSECURITY-

# Instalar dependencias
pip install -r requirements.txt
```

## 🎯 Uso

```bash
python app.py
```

Luego abre en tu navegador: **http://localhost:5000**

**Credenciales por defecto:**
- Usuario: `admin`
- Contraseña: `admin123`

## 📊 Dashboard

El dashboard muestra en tiempo real:

- **Estadísticas** - Total de amenazas por severidad
- **Tabla de eventos** - Detalles de cada intento detectado
- **Clasificación** - Tipo de amenaza (escaneo, inyección, malware, etc)
- **Severidad** - Nivel de riesgo (baja, media, alta, crítica)

## 🤖 Tipos de Amenazas Detectadas

- 🔍 **Escaneo** - Intentos de descubrir servicios (Nmap, etc)
- 💉 **Inyección** - SQL injection, command injection
- 🔐 **Acceso Remoto** - SSH, RDP, Telnet
- 🦠 **Malware** - Ejecución de código malicioso
- ❌ **XSS** - Cross-site scripting
- 💥 **DDoS** - Ataques de denegación de servicio

## 📁 Estructura

```
.
├── app.py                    # Aplicación Flask principal
├── auth.py                   # Autenticación de usuarios
├── database.py               # Modelos y funciones de BD
├── honeypot.py               # Servidor honeypot
├── ai_threats.py             # Analizador de IA
├── requirements.txt          # Dependencias
├── templates/
│   ├── dashboard.html        # Dashboard principal
│   └── login.html            # Página de login
└── README.md                 # Este archivo
```

## 🔧 API Endpoints

- `GET /` - Dashboard principal (requiere login)
- `GET /api/threats` - Obtener amenazas detectadas
- `GET /api/stats` - Obtener estadísticas
- `POST /login` - Autenticación de usuario
- `GET /logout` - Cerrar sesión

## 📈 Ejemplo de Respuesta

```json
{
  "total_amenazas": 15,
  "criticas": 3,
  "altas": 5,
  "medias": 4,
  "bajas": 3
}
```

## 🛡️ Seguridad

- ✅ Autenticación con contraseña encriptada
- ✅ El honeypot no accede a información real
- ✅ Solo monitorea intentos de conexión
- ✅ Los datos se almacenan localmente
- ✅ Aislado del resto del sistema
- ✅ Protección de sesiones

## 💾 Base de Datos

Los eventos se guardan en `threats.db` (SQLite) con:
- Fecha y hora del ataque
- IP atacante
- Puerto objetivo
- Tipo de amenaza detectada
- Nivel de severidad

## 🚦 Estado del Proyecto

✅ Honeypot funcional
✅ Análisis de IA
✅ Dashboard web
✅ Base de datos SQLite
✅ Autenticación y login
🔄 En desarrollo continuo

## 📄 Licencia

GNU General Public License v3.0

## 👨‍💻 Autor

**Taks1221** - Proyecto de Ciberseguridad HIBRID TECHNOLOGIES

---

**¿Necesitas ayuda?** Abre un issue o contacta al equipo de desarrollo.
