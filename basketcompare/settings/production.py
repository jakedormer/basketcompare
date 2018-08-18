from .base import *
import django_heroku
import os

DEBUG = False

ROOT_URLCONF = 'basketcompare.urls.url_production'

django_heroku.settings(locals())

SECRET_KEY = os.getenv('SECRET_KEY')


ALLOWED_HOSTS = [
	'hidden-sands-73111.herokuapp.com',
	'basketcompare.co.uk',
]



EMAIL_HOST_USER = os.environ['SENDGRID_PASSWORD']
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_USERNAME']
SERVER_EMAIL = 'django@hidden-sands-73111.herokuapp.com'

MEDIA_URL = 'https://s3.eu-west-2.amazonaws.com/basketcompare-core/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "staticfiles", "media")