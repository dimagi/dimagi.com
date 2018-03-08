import os
import environ

root = environ.Path(os.path.dirname(os.path.abspath(__file__)))
base_dir = environ.Path(os.path.dirname(os.path.dirname(__file__)))
env = environ.Env()
env.read_env('.env')  # also reads from os.environ

BASE_DIR = base_dir()
PROJECT_ROOT = root()

APPEND_SLASH = True

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
    'compressor',
    'imagekit',
]
if AWS_ENABLED:
    THIRD_PARTY_APPS.append('storages')

PROJECT_APPS = [
    'dimagi.utils',
    'dimagi.pages',
    'dimagi.blog',
    'dimagi.careers',
    'dimagi.case_studies',
    'dimagi.press',
    'dimagi.toolkits',
    'dimagi.sectors',
]
INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

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
                'dimagi.utils.context_processors.metas',
                'dimagi.utils.context_processors.external_urls',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
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

DEPLOY_ENVIRONMENT = env.str('DEPLOY_ENVIRONMENT', default='dev')

CACHES = {
    'default': env.cache('REDIS_URL'),
}

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
    'compressor.finders.CompressorFinder',
]

STATIC_ROOT = root('staticfiles')
STATIC_URL = env.str('STATIC_URL', default='/static/')

SASS_ASSETS = static_assets_root('style')
SASS_PROCESSOR_INCLUDE_DIRS = [
    SASS_ASSETS,
    static_libs('bourbon/app/assets/stylesheets'),
]
SASS_PRECISION = 8
SASS_PROCESSOR_ENABLED = True

AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME', default='')
AWS_CLOUDFRONT_DOMAIN = env.str('AWS_CLOUDFRONT_DOMAIN', default='')
AWS_CLOUDFRONT_DISTRIBUTION_ID = env.str('AWS_CLOUDFRONT_DISTRIBUTION_ID', default='')

if AWS_ENABLED:
    AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID', default='')
    AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY', default='')
    AWS_S3_REGION_NAME = env.str('AWS_S3_REGION_NAME', default='')
    AWS_S3_CUSTOM_DOMAIN = AWS_CLOUDFRONT_DOMAIN
    AWS_LOCATION = STATIC_URL

COMPRESS_CSS_FILTERS = (
    'compressor_postcss.PostCSSFilter',
    'dimagi.compress.ImagekitCssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
)
COMPRESS_POSTCSS_PLUGINS = (
    'autoprefixer',
)
COMPRESS_ENABLED = env.bool('COMPRESS_ENABLED', default=True)
COMPRESS_OFFLINE = env.bool('COMPRESS_OFFLINE', default=True)

if AWS_CLOUDFRONT_DOMAIN:
    STATIC_CDN = "//{}".format(AWS_CLOUDFRONT_DOMAIN)
else:
    STATIC_CDN = ''

COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_CDN + STATIC_URL
COMPRESS_CSS_HASHING_METHOD = 'content'

if AWS_ENABLED:
    STATICFILES_STORAGE = "dimagi.storage.StaticFileStorage"
    COMPRESS_STORAGE = "dimagi.storage.CachedS3BotoStorage"
    COMPRESS_CSS_COMPRESSOR = 'dimagi.compress.S3CssCompressor'

WORDPRESS_API_URL = env.str('WORDPRESS_API_URL', default='')
WORDPRESS_API_USER_AGENT = env.str(
    'WORDPRESS_API_USER_AGENT',
    default='dimagidotcom/prod'
)

SITE_URL = env.str('SITE_URL', default='http://dimagi.com')

# analytics
TRACKING = {
    'GOOGLE': env.str('GOOGLE', default=''),
    'HUBSPOT': env.str('HUBSPOT', default=''),
    'KISSMETRICS': env.str('KISSMETRICS', default=''),
    'DRIFT': env.str('DRIFT', default=''),
}

TRACKING_LOG_LEVEL = env.str('TRACKING_LOG_LEVEL', default='')
TRACKING_ENABLED = env.bool('TRACKING_ENABLED', default=False)
