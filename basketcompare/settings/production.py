from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['hidden-sands-73111.herokuapp.com']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

django_heroku.settings(locals())

EMAIL_HOST_USER = SENDGRID_PASSWORD
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = SENDGRID_USERNAME
SERVER_EMAIL = 'django@hidden-sands-73111.herokuapp.com'

