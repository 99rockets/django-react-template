from .base import *

DEBUG = True

REUSE_DB = 1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# This is for local development
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/local/',  # end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-local.json'),
    }
}
