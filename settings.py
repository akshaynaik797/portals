import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'config.env')
load_dotenv(dotenv_path)

API_SERVER_URL = os.environ.get("API_SERVER_URL")
WEBDRIVER_FOLDER_PATH = os.environ.get("WEBDRIVER_FOLDER_PATH")
WAIT_PERIOD = os.environ.get("WAIT_PERIOD")
DBNAME = os.environ.get("DBNAME")
pass
