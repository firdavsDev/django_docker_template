from .base import *  # noqa

SERVER_IP = os.environ["SERVER_IP"]
SERVER_DOMAIN = os.environ["SERVER_DOMAIN"]

DEBUG = os.environ["DEBUG"]

ALLOWED_HOSTS = [SERVER_IP, SERVER_DOMAIN]


SPECTACULAR_SETTINGS["SERVERS"] = [  # noqa: F405
    {"url": "https://warehouse.karantin.uz", "description": "Production server"},
]

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = os.environ["DJANGO_SECURE_SSL_REDIRECT"]
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ["DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS"]
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = os.environ["DJANGO_SECURE_HSTS_PRELOAD"]
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = os.environ["DJANGO_SECURE_CONTENT_TYPE_NOSNIFF"]

# STATIC
# ------------------------
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
