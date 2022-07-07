import dj_database_url
from decouple import config
from pathlib import Path

# fetch Django's project directory
DJANGO_ROOT = Path(__file__).resolve().parent.parent

# fetch the project_root
PROJECT_ROOT = DJANGO_ROOT.parent


# the name of the whole site
SITE_NAME = DJANGO_ROOT.name

# collect static files here
STATIC_ROOT = PROJECT_ROOT / 'run' / 'static'

# collect media files here
MEDIA_ROOT = PROJECT_ROOT / 'run' / 'media'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# look for static assets here
STATICFILES_DIRS = [
    PROJECT_ROOT / 'static',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES = [
    PROJECT_ROOT / 'templates',
]



# ##### APPLICATION CONFIGURATION #########################

# these are the apps
INSTALLED_APPS = [
    'config.apps.users',

    'django_extensions',
    'phonenumber_field',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# template stuff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            DJANGO_ROOT / 'templates',
            PROJECT_TEMPLATES
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Internationalization
USE_I18N = False

# ##### SECURITY CONFIGURATION ############################

# We store the secret key here
# The required SECRET_KEY is fetched at the end of this file
# SECRET_FILE = normpath(join(PROJECT_ROOT, 'run', 'SECRET.key'))

# these persons receive error notification
admin_name = config('ADMIN_NAME')
admin_email = config('ADMIN_EMAIL')
ADMINS = (
    (admin_name, admin_email),
)
MANAGERS = ADMINS

# ##### DJANGO RUNNING CONFIGURATION ######################

# the default WSGI application
WSGI_APPLICATION = 'config.wsgi.application'

# the root URL configuration
ROOT_URLCONF = 'config.urls'

# the URL for static files
STATIC_URL = '/static/'

# the URL for media files
MEDIA_URL = '/media/'

# ##### DEBUG CONFIGURATION ###############################
DEBUG = False


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600,
        ssl_require=False
    )
}

# Custom Authentication

AUTH_USER_MODEL = 'users.User'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'