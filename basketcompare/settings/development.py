from .base import *

DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_URL = '/static/'
MEDIA_URL = 'static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "staticfiles", "media")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    )
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")