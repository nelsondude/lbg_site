from .base import *

# set for heroku puproses
DEBUG = True

SECURE_SSL_REDIRECT = True
PREPEND_WWW = True

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
