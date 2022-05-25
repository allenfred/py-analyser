import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".ini"))

API_KEY = config["OKEX"]["API_KEY"]
API_SECRET = config["OKEX"]["API_SECRET"]
PASSPHRASE = config["OKEX"]["PASSPHRASE"]
DB_HOST = config["DEFAULT"]["DB_HOST"]
DB_USERNAME = config["DEFAULT"]["DB_USERNAME"]
DB_PASSWORD = config["DEFAULT"]["DB_PASSWORD"]
DB_NAME = config["DEFAULT"]["DB_NAME"]
