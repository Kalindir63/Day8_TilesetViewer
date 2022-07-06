from .base import *

SECRET_KEY = 'dev'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Static Files dir
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'
