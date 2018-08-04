from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['hidden-sands-73111.herokuapp.com']

django_heroku.settings(locals())
