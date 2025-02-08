from myproject.settings import *
import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# INSTALLED_APPS = []

# sites framework

SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / "assets",
]



# forgot password authentication
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'



#tinyMCE

TINYMCE_DEFAULT_CONFIG = {
    'height': 500,
    'width': '100%',
    'plugins': 'image code link lists',
    'toolbar': 'undo redo | formatselect | bold italic underline | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | code',
    'image_advtab': True,
    'images_upload_url': '/tinymce-upload/',
    'automatic_uploads': True,
}


# django debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]
