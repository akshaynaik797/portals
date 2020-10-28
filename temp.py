import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'config.env')
load_dotenv(dotenv_path)

USERNAME = os.environ.get("username")
SECRET_KEY = os.environ.get("password")
pass