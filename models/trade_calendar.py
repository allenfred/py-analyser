# 导入:
from sqlalchemy import Table, MetaData, Column, Integer, String, Date, SmallInteger, select, or_, asc, desc
from sqlalchemy.ext.declarative import declarative_base
from .db import engine, DBSession
from datetime import date, datetime, timedelta
import pandas as pd

Base = declarative_base()
metadata_obj = MetaData()

trade_calendar = Table('trade_calendar', metadata_obj,
                       Column('id', Integer, primary_key=True),
                       Column('exchange', String),
                       Column('cal_date', Date),
                       Column('is_open', SmallInteger),
                       Column('pretrade_date', Date),
                       Column('candle_ready', SmallInteger),
                       Column('basic_ready', SmallInteger),
                       )


def get_obj(calendar):
    obj = TradeCalendar(
        exchange=calendar.get('exchange', None),
        cal_date=calendar.get('cal_date', None),
        is_open=calendar.get('is_open', None),
        pretrade_date=calendar.get('pretrade_date', None),
        candle_ready=calendar.get('candle_ready', 0),
        basic_ready=calendar.get('basic_ready', 0),
    )

    return obj


# 定义 TradeCalendar 对象:
class TradeCalendar(Base):
    # 表的名字:
    __tablename__ = 'trade_calendar'

    # 表的结构:
    id = Column(Integer, autoincrement=True, primary_key=True)
    exchange = Column(String(20))  # 交易所: SSE上交所 SZSE深交所 HK港交所 US美交所
    cal_date = Column(Date)  # 日历日期
    is_open = Column(SmallInteger)  # 是否交易 0休市 1交易
    pretrade_date = Column(Date)  # 上一个交易日
    candle_ready = Column(SmallInteger)  # 日K是否获取完成 0否 1是
    basic_ready = Column(SmallInteger)  # 每日指标是获取完成 0否 1是


class TradeCalendarDao:
    def __init__(self):
        self.session = DBSession()

    def add_one(self, calendar):
        obj = get_obj(calendar)

        row = self.session.query(TradeCalendar).filter(TradeCalendar.exchange == calendar['exchange']).filter(
            TradeCalendar.cal_date == calendar['cal_date']).first()

        if row:
            self.session.add(obj)
        else:
            if obj.is_open is not None:
                row.is_open = obj.is_open
            if obj.pretrade_date is not None:
                row.pretrade_date = obj.pretrade_date
            if obj.candle_ready is not None:
                row.candle_ready = obj.candle_ready
            if obj.basic_ready is not None:
                row.basic_ready = obj.basic_ready

        self.session.commit()
        self.session.close()

        return obj

    def bulk_upsert(self, df):

        for index, calendar in df.iterrows():
            obj = get_obj(calendar)

            row = self.session.query(TradeCalendar).filter(TradeCalendar.exchange == calendar['exchange']).filter(
                TradeCalendar.cal_date == calendar['cal_date']).first()

            if row is None:
                self.session.add(obj)
            else:
                if obj.is_open is not None:
                    row.is_open = obj.is_open
                if obj.pretrade_date is not None:
                    row.pretrade_date = obj.pretrade_date
                if obj.candle_ready is not None:
                    row.candle_ready = obj.candle_ready
                if obj.basic_ready is not None:
                    row.basic_ready = obj.basic_ready

        self.session.commit()
        self.session.close()

        return df

    def bulk_insert(self, df):
        items = []
        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        self.session.bulk_insert_mappings(TradeCalendar, items)
        self.session.commit()
        self.session.close()

    def find_one_candle_not_ready(self, exchange):

        with engine.connect() as conn:
            today = date.today().strftime("%Y-%m-%d")
            if exchange == 'CN':
                exchange = 'SSE'

            if exchange == 'US':
                today = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")

            stmts = select(trade_calendar).where(
                trade_calendar.c.exchange == exchange,
                trade_calendar.c.candle_ready != 1,
                trade_calendar.c.is_open == 1,
                trade_calendar.c.cal_date >= '2015-01-01',
                trade_calendar.c.cal_date <= today).order_by(trade_calendar.c.cal_date).limit(1)

            rows = conn.execute(stmts).fetchall()

            if len(rows) > 0:
                return rows[0]
            else:
                return None

    def set_cn_candle_ready(self, dte):
        with engine.connect() as conn:
            conn.execute(trade_calendar.update().values(candle_ready=1).where(trade_calendar.c.cal_date == dte). \
                         where(or_(trade_calendar.c.exchange == 'SSE', trade_calendar.c.exchange == 'SZSE')))

    def set_hk_candle_ready(self, dte):
        with engine.connect() as conn:
            conn.execute(trade_calendar.update().values(candle_ready=1). \
                         where(trade_calendar.c.cal_date == dte, trade_calendar.c.exchange == 'HK'))

    def set_us_candle_ready(self, dte):
        with engine.connect() as conn:
            conn.execute(trade_calendar.update().values(candle_ready=1). \
                         where(trade_calendar.c.cal_date == dte, trade_calendar.c.exchange == 'US'))
