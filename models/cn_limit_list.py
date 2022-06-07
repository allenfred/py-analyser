from sqlalchemy import Column, Integer, String, Date, Time, Float, select, text, update, bindparam
from sqlalchemy.ext.declarative import declarative_base
from .db import engine, DBSession
import pandas as pd

Base = declarative_base()


class CNLimitList(Base):
    __tablename__ = 'cn_limit_list'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    name = Column(String)  # 股票名称
    trade_date = Column(Date)  # 交易日期
    close = Column(Float)  # 收盘价
    pct_chg = Column(Float)  # 涨跌幅
    amp = Column(Float)  # 振幅
    vol = Column(Float)  # 成交量
    fc_ratio = Column(Float)  # 封单金额/日成交金额
    fl_ratio = Column(Float)  # 封单手数/流通股本
    fd_amount = Column(Float)  # 封单金额
    first_time = Column(Time)  # 首次涨停时间
    last_time = Column(Time)  # 最后封板时间
    open_times = Column(Integer)  # 打开次数
    strth = Column(Float)  # 涨跌停强度
    limit = Column(String)  # D跌停U涨停


def get_obj(candle):
    candle = candle.to_dict()
    candle = {k: v if not pd.isna(v) else None for k, v in candle.items()}

    return CNLimitList(
        ts_code=candle.get('ts_code', None),
        trade_date=candle.get('trade_date', None),
        name=candle.get('name', None),
        close=candle.get('close', None),
        pct_chg=candle.get('pct_chg', None),
        amp=candle.get('amp', None),
        fc_ratio=candle.get('fc_ratio', None),
        fl_ratio=candle.get('fl_ratio', None),
        fd_amount=candle.get('fd_amount', None),
        first_time=candle.get('first_time', None),
        last_time=candle.get('last_time', None),
        open_times=candle.get('open_times', None),
        strth=candle.get('strth', None),
        limit=candle.get('limit', None),
    )


class CNLimitListDao:
    def __init__(self):
        self.session = DBSession()

    def reinsert(self, df):
        trade_date = df['trade_date'][0]
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.execute("delete from cn_limit_list where trade_date = :trade_date",
                                 {"trade_date": trade_date})
            self.session.bulk_insert_mappings(CNLimitList, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()
        return len(df)
