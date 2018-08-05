from .base import *
import django_heroku
from boto.s3.connection import S3Connection

DEBUG = False
SECRET_KEY = S3Connection(os.environ['SECRET_KEY'])

ALLOWED_HOSTS = ['hidden-sands-73111.herokuapp.com']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

django_heroku.settings(locals())

EMAIL_HOST_USER = S3Connection(os.environ['SENDGRID_PASSWORD'])
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = S3Connection(os.environ['SENDGRID_USERNAME'])
SERVER_EMAIL = 'django@hidden-sands-73111.herokuapp.com'

