import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".ini"))

TS_TOKEN = config["DEFAULT"]["TOKEN"]
