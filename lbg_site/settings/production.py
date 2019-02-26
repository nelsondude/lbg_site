from .base import *

# set for heroku puproses
DEBUG = True

SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
