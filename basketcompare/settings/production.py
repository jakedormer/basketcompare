from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['hidden-sands-73111.herokuapp.com']

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

django_heroku.settings(locals())

EMAIL_HOST_USER = 'app104453826@heroku.com'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = 'vr3fnnr76312'
SERVER_EMAIL = 'django@hidden-sands-73111.herokuapp.com'

