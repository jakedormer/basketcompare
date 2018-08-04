from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['hidden-sands-73111.herokuapp.com']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

django_heroku.settings(locals())

EMAIL_HOST_USER = 'app104453826@heroku.com'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = 'vr3fnnr76312'
SERVER_EMAIL = 'django@hidden-sands-73111.herokuapp.com'

