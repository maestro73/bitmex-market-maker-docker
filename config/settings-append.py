
import os

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

if os.getenv('WATCH_CUSTOM_SETTINGS') in ['True', 'true', 'Yes', 'yes', 'Y', 'y']:
    WATCHED_FILES.append(join('config', 'settings.py'))

from config.settings import *
