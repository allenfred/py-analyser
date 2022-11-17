import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".ini"))

TS_TOKEN = config["DEFAULT"]["TS_TOKEN"]

# CRYPTO
OKX_API_KEY = config["OKEX"]["API_KEY"]
OKX_API_SECRET = config["OKEX"]["API_SECRET"]
OKX_PASSPHRASE = config["OKEX"]["PASSPHRASE"]
CRYPTO_DB_HOST = config["DEFAULT"]["CRYPTO_DB_HOST"]
CRYPTO_DB_USERNAME = config["DEFAULT"]["CRYPTO_DB_USERNAME"]
CRYPTO_DB_PASSWORD = config["DEFAULT"]["CRYPTO_DB_PASSWORD"]
CRYPTO_DB_NAME = config["DEFAULT"]["CRYPTO_DB_NAME"]

# SCAN Setting
START_INDEX = 200
