from .base import *

# set for heroku puproses
DEBUG = True

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
