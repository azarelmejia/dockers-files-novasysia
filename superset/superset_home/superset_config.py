# ==========================================
# 🧠 Superset Custom Configuration (Nova SysIA)
# ==========================================

# Modo público controlado
PUBLIC_ROLE_LIKE = "Public"

# Habilitar modo embed seguro (opcional)
ENABLE_JWT_EMBEDDING = True

# Corregir proxy reverse (Traefik)
ENABLE_PROXY_FIX = True

# Timezone
SUPERSET_WEBSERVER_TIMEOUT = 300
SUPERSET_WEBSERVER_THREADS = 8

# (Opcional) Logs y cache
LOG_LEVEL = "INFO"

# Configuración básica para evitar errores de sesión
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = True

# Idioma y zona horaria
LANGUAGES = {
    "en": {"flag": "us", "name": "English"},
    "es": {"flag": "es", "name": "Español"},
}
