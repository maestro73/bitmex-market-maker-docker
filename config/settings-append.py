
import os

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

WATCHED_FILES.append(join('config', 'settings.py'))
from config.settings import *
