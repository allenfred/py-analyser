#  -*- coding: utf-8 -*-
import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

from pymongo import MongoClient
from config.common import CRYPTO_DB_HOST, CRYPTO_DB_NAME, CRYPTO_DB_PASSWORD, CRYPTO_DB_USERNAME
from bson.raw_bson import RawBSONDocument
from bson.codec_options import CodecOptions
import pytz

connection = MongoClient(CRYPTO_DB_HOST, document_class=RawBSONDocument)
db = connection[CRYPTO_DB_NAME]
db.authenticate(CRYPTO_DB_USERNAME, CRYPTO_DB_PASSWORD)

InstrumentInfos = db["instrument_infos"]
UsdtSwapKlines = db["usdt_swap_klines"].with_options(
    codec_options=CodecOptions(tz_aware=True, tzinfo=pytz.timezone("Etc/GMT+8"))
)
