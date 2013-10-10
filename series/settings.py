import os

import dj_database_url


DEBUG = os.environ.get('DEBUG', False)
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Marc Tamlyn', 'marc.tamlyn@gmail.com'),
)
MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config(default='postgres://localhost/agbns')}

SECRET_KEY = os.environ.get('SECRET_KEY', 'asdfasd;lfkjasf')
ALLOWED_HOSTS = ['.mjtamlyn.co.uk']

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-gb'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.AppDirectoriesFinder',)

TEMPLATE_LOADERS = ('django.template.loaders.app_directories.Loader',)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'series.urls'
WSGI_APPLICATION = 'series.wsgi.application'

INSTALLED_APPS = (
    'series',

    'feincms',
    'feincms.module.page',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
