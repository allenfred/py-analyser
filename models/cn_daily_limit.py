from sqlalchemy import Column, Integer, String, Date, DateTime, Float, select, text, update, bindparam
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import literal_column
from .db import engine, DBSession
import pandas as pd
from datetime import datetime, date
import mysql.connector

Base = declarative_base()


class CNDailyLimit(Base):
    __tablename__ = 'cn_daily_limit'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    trade_date = Column(Date)  # 交易日期
    pre_close = Column(Float)  # 昨日收盘价
    up_limit = Column(Float)  # 涨停价
    down_limit = Column(Float)  # 跌停价


def get_obj(candle):
    candle = candle.to_dict()
    candle = {k: v if not pd.isna(v) else None for k, v in candle.items()}

    return CNDailyLimit(
        ts_code=candle.get('ts_code', None),
        trade_date=candle.get('trade_date', None),
        pre_close=candle.get('pre_close', None),
        up_limit=candle.get('up_limit', None),
        down_limit=candle.get('down_limit', None),
    )


class CNDailyLimitDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_trade_date(self, trade_date):
        s = text("select ts_code, trade_date, up_limit, down_limit from cn_daily_limit where trade_date = :trade_date;")
        statement = self.session.execute(s.params(trade_date=trade_date))
        df = pd.DataFrame(statement.fetchall(), columns=['ts_code', 'trade_date', 'up_limit', 'down_limit'])
        self.session.close()

        return df

    def reinsert(self, df):
        trade_date = df['trade_date'][0]
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.execute("delete from cn_daily_limit where trade_date = :trade_date",
                                 {"trade_date": trade_date})
            self.session.bulk_insert_mappings(CNDailyLimit, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()
        return len(df)
