from .base import *

DEBUG = True
SECRET_KEY = ['kse8ckn79d_dznk)&!x0u7c%+qx1zh#qtgqwaxqfxvrn7ni_9y']
ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


JD = ""