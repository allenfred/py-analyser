#  -*- coding: utf-8 -*-

from pymongo import MongoClient
from config.common import DB_HOST, DB_NAME, DB_PASSWORD, DB_USERNAME
from bson.raw_bson import RawBSONDocument
from bson.codec_options import CodecOptions
import pytz

connection = MongoClient(DB_HOST, document_class=RawBSONDocument)
db = connection[DB_NAME]
db.authenticate(DB_USERNAME, DB_PASSWORD)

InstrumentInfos = db["instrument_infos"]
UsdtSwapKlines = db["usdt_swap_klines"].with_options(
    codec_options=CodecOptions(tz_aware=True, tzinfo=pytz.timezone("Etc/GMT+8"))
)
