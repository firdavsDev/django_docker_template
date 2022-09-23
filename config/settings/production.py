from .base import *  # noqa

SERVER_IP = os.environ["SERVER_IP"]
SERVER_DOMAIN = os.environ["SERVER_DOMAIN"]

DEBUG = os.environ["DEBUG"]

ALLOWED_HOSTS = [SERVER_IP, SERVER_DOMAIN]
