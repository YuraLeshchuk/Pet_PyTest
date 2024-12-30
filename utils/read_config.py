import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "../config/config.ini")
config.read(config_path)

def get_url():
    url = config.get('environment', 'base_url')
    return url