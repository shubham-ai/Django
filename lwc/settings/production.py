import os
from django.config import settings


DEBUG = False
TEMPLATE_DEBUG=True


import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']



try:
    from .local_settings import *
except ImportError:
    pass

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL='/static'

# STATICFILES_DIRS=(
# 	os.path.join(BASE_DIR,'static'),
# 	)