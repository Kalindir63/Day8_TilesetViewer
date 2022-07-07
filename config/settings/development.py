from .common import *

SECRET_KEY = 'dev'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Static Files dir
STATIC_ROOT = PROJECT_ROOT / 'staticfiles'

STATIC_URL = '/static/'

MEDIA_ROOT = PROJECT_ROOT / 'media'

MEDIA_URL = '/media/'
