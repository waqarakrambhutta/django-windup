import os
from .common import *

DEBUG = False # If debug is off them we need to add the setting allowed hosts below.

SECURITY_KEY = os.environ('SECURITY_KEY')

ALLOWED_HOSTS = []