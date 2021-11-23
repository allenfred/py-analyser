# -- coding: utf-8 -
import os
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)

from sqlalchemy import text
import pandas as pd
import time
from datetime import datetime, date
import numpy as np

from models.db import DBSession
from models.stocks import StockDao
from api.daily_basic import get_cn_daily_basic

stockDao = StockDao()

if __name__ == "__main__":

    df = get_cn_daily_basic('20211122')
    for index, row in df.iterrows():
        stockDao.update(row.to_dict())
    # print(df)
