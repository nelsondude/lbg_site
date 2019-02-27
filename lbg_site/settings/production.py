from .base import *

# set for heroku puproses
DEBUG = True

SECURE_SSL_REDIRECT = True
# PREPEND_WWW = True

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
