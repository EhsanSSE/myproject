from myproject.settings import *
import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() in ["true", "1", "yes", "True"]

ALLOWED_HOSTS = ['ehsanshirvani.ir', 'www.ehsanshirvani.ir', 'flio.liara.run']

# INSTALLED_APPS = []

# sites framework

SITE_ID = 4

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':     os.getenv("POSTGRESQL_DB_NAME"), 
        'USER':     os.getenv("POSTGRESQL_DB_USER"),
        'PASSWORD': os.getenv("POSTGRESQL_DB_PASS"),
        'HOST':     os.getenv("POSTGRESQL_DB_HOST"),
        'PORT':     os.getenv("POSTGRESQL_DB_PORT"),
    },
}


MEDIA_ROOT = '/usr/src/app/media'
STATIC_ROOT = '/usr/src/app/static'

STATICFILES_DIRS = [
    BASE_DIR / "assets",
]


# Email
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'False').lower() in ["true", "1", "yes", "True"]
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True 
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True


# robots module

ROBOTS_USE_SITEMAP = True
ROBOTS_USE_HOST = True

MIGRATION_MODULES = {
    'main': 'migrations.main',
    'blog': 'migrations.blog',
}