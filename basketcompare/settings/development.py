from .base import *

DEBUG = True
SECRET_KEY = ['kse8ckn79d_dznk)&!x0u7c%+qx1zh#qtgqwaxqfxvrn7ni_9y']
ROOT_URLCONF = 'basketcompare.urls.url_development'
ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'testing@example.com'


MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "staticfiles", "media")

# make all loggers use the console.


