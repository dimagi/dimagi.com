import os
import environ

root = environ.Path(os.path.dirname(os.path.abspath(__file__)))
base_dir = environ.Path(os.path.dirname(os.path.dirname(__file__)))
env = environ.Env()
env.read_env('.env')  # also reads from os.environ

BASE_DIR = base_dir()
PROJECT_ROOT = root()

SECRET_KEY = env('SECRET_KEY', default='changeme')
DEBUG = env.bool('DEBUG', default=False)
AWS_ENABLED = env.bool('AWS_ENABLED', default=False)

DEFAULT_APPS = [
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'sass_processor',
]
if AWS_ENABLED:
    THIRD_PARTY_APPS.append('storages')

PROJECT_APPS = [
    'dimagi.utils',
    'dimagi.pages',
]
INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'dimagi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'dimagi.utils.context_processors.global_vars',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'dimagi.wsgi.application'

# We aren't going to use a database just yet. Simplify.
DATABASES = {}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
static_assets_root = root.path('assets/')
STATIC_ASSETS = static_assets_root()
static_libs = root.path('node_modules/')
STATICFILES_DIRS = (
    STATIC_ASSETS,
    ('js/lib/blazy', static_libs('blazy')),
    ('js/lib/jquery', static_libs('jquery/dist')),
    ('js/lib/knockout', static_libs('knockout/build/output')),
    ('js/lib/lodash', static_libs('lodash')),
    ('js/lib/requirejs', static_libs('requirejs')),
)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

STATIC_ROOT = root('staticfiles')
STATIC_URL = env.str('STATIC_URL', default='/static/')
STATIC_CDN = env.str('STATIC_CDN', default='')

if AWS_ENABLED:
    STATICFILES_STORAGE = env.str('STATICFILES_STORAGE', default='dimagi.storage.CachedS3BotoStorage')
    COMPRESS_STORAGE = STATICFILES_STORAGE

SASS_ASSETS = static_assets_root('style')
SASS_PROCESSOR_INCLUDE_DIRS = [
    SASS_ASSETS,
    static_libs('bourbon/app/assets/stylesheets'),
]
SASS_PRECISION = 8
SASS_PROCESSOR_ENABLED = True

AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME', default='')

if AWS_ENABLED:
    AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID', default='')
    AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY', default='')
    AWS_S3_REGION_NAME = env.str('AWS_S3_REGION_NAME', default='')
    AWS_S3_CUSTOM_DOMAIN = env.str('AWS_S3_CUSTOM_DOMAIN', default='')
    AWS_LOCATION = STATIC_URL

CACHES = {
    'default': env.cache('REDIS_URL'),
}
