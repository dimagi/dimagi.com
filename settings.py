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
    'django.contrib.sitemaps',
]

THIRD_PARTY_APPS = [
    'sass_processor',
    'require',
    'compressor',
    'imagekit',
    'capture_tag',
    'django_user_agents',
]
if AWS_ENABLED:
    THIRD_PARTY_APPS.append('storages')

PROJECT_APPS = [
    'dimagi.utils',
    'dimagi.data',
    'dimagi.pages',
    'dimagi.styleguide',
]
INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

DEPLOY_ENVIRONMENT = env.str('DEPLOY_ENVIRONMENT', default='dev')

if DEPLOY_ENVIRONMENT != 'production':
    MIDDLEWARE.append('dimagi.utils.middleware.no_index_middleware')

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
                'dimagi.utils.context_processors.ab_tests',
                'dimagi.utils.context_processors.hubspot_ctas',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'dimagi.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('DATABASE_NAME', default=''),
        'USER': env.str('DATABASE_USER', default=''),
        'PASSWORD': env.str('DATABASE_PASSWORD', default=''),
        'HOST': env.str('DATABASE_HOST', default=''),
        'PORT': env.str('DATABASE_PORT', default=''),
    },
}

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

HEROKU_REDIS_URL = 'HEROKU_REDIS_TEAL_TLS_URL' if DEPLOY_ENVIRONMENT == 'production' else 'REDIS_URL'

CACHES = {
    'default': env.cache(HEROKU_REDIS_URL),
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
    ('js/lib/select2', static_libs('select2')),
)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
]
STATICFILES_STORAGE = 'require.storage.OptimizedStaticFilesStorage'

STATIC_ROOT = root('staticfiles')
STATIC_URL = env.str('STATIC_URL', default='/static/')

SASS_ASSETS = static_assets_root('style')
SASS_PROCESSOR_INCLUDE_DIRS = [
    SASS_ASSETS,
    static_libs('bourbon/app/assets/stylesheets'),
]
SASS_PRECISION = 8
SASS_PROCESSOR_ENABLED = True

REQUIRE_BASE_URL = "js"
REQUIRE_JS = "require.js"
REQUIRE_BUILD_PROFILE = "app.build.js"
REQUIRE_STANDALONE_MODULES = {}
REQUIRE_DEBUG = DEBUG

AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME', default='')
AWS_CLOUDFRONT_DOMAIN = env.str('AWS_CLOUDFRONT_DOMAIN', default='')
AWS_CLOUDFRONT_DISTRIBUTION_ID = env.str('AWS_CLOUDFRONT_DISTRIBUTION_ID', default='')
AWS_IS_GZIPPED = env.bool('AWS_IS_GZIPPED', default=False)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

if AWS_ENABLED:
    AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID', default='')
    AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY', default='')
    AWS_S3_REGION_NAME = env.str('AWS_S3_REGION_NAME', default='')
    AWS_S3_CUSTOM_DOMAIN = AWS_CLOUDFRONT_DOMAIN
    AWS_LOCATION = STATIC_URL

COMPRESS_CSS_FILTERS = (
    'compressor_postcss.PostCSSFilter',
    'compressor.filters.css_default.CssAbsoluteFilter',
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

SITE_URL = env.str('SITE_URL', default='https://dimagi.com')

# analytics
ANALYTICS = {
    'GTM': env.str('GTM', default=''),
    'HUBSPOT': env.str('HUBSPOT', default=''),
    'KISSMETRICS': env.str('KISSMETRICS', default=''),
    'DRIFT': env.str('DRIFT', default=''),
}

AUDIT_AB_CLICKS = env.bool('AUDIT_AB_CLICKS', default=False)

ANALYTICS_LOG_LEVEL = env.str('ANALYTICS_LOG_LEVEL', default='')
ANALYTICS_ENABLED = env.bool('ANALYTICS_ENABLED', default=False)

FRIENDBUY_ACCESS = env.str('FRIENDBUY_ACCESS', default='')
FRIENDBUY_SECRET = env.str('FRIENDBUY_SECRET', default='')

HUBSPOT_API_KEY = env.str('HUBSPOT_API_KEY', default='')
