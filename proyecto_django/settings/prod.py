from .base import *
import dj_database_url
import os

DEBUG = False

ALLOWED_HOSTS = ['.onrender.com', '*']

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# Seguridad
CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com']
SECURE_SSL_REDIRECT = True


# === Configuración de archivos estáticos ===
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Archivos multimedia (si usas MEDIA en algún lado)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'