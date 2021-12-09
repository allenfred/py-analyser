from sqlalchemy import Column, Integer, String, Date, Float, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class WeeklyCandle(Base):
    __tablename__ = 'weekly_candles'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    trade_date = Column(Date)  # 交易日期
    open = Column(Float)  # 开盘价
    high = Column(Float)  # 最高价
    low = Column(Float)  # 最低价
    close = Column(Float)  # 收盘价
    pre_close = Column(Float)  # 昨收价
    change = Column(Float)  # 涨跌额
    pct_chg = Column(Float)  # 涨跌幅
    vol = Column(Float)  # 成交量
    amount = Column(Float)  # 成交额


def get_obj(candle):
    candle = candle.to_dict()
    candle = {k: v if not pd.isna(v) else None for k, v in candle.items()}

    return WeeklyCandle(
        ts_code=candle.get('ts_code', None),
        trade_date=candle.get('trade_date', None),
        open=candle.get('open', None),
        high=candle.get('high', None),
        low=candle.get('low', None),
        close=candle.get('close', None),
        pre_close=candle.get('pre_close', None),
        change=candle.get('change', None),
        pct_chg=candle.get('pct_chg', None),
        vol=candle.get('vol', None),
        amount=candle.get('amount', None)
    )


class WeeklyCandleDao:
    def __init__(self):
        self.session = DBSession()

    def find_latest_candle(self):
        s = text("select trade_date, open, close, high, low from weekly_candles order by trade_date desc limit 1;")
        statement = self.session.execute(s.params())
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'close', 'high', 'low'])
        self.session.close()

        if len(df):
            return df.iloc[0]
        else:
            return None

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date, open, close, high, low from weekly_candles where ts_code = :ts_code "
                 "order by trade_date desc limit 0,600;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'close', 'high', 'low'])
        self.session.close()

        return df

    def find_by_trade_date(self, trade_date):
        s = text("select ts_code, open, close, high, low from weekly_candles where trade_date = :trade_date;")
        statement = self.session.execute(s.params(trade_date=trade_date))
        df = pd.DataFrame(statement.fetchall(), columns=['ts_code', 'open', 'close', 'high', 'low'])
        self.session.close()

        return df

    def bulk_insert(self, df):
        items = []
        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}

            if item['ts_code'] is not None and item['trade_date'] is not None:
                items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(WeeklyCandle, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def reinsert(self, df):
        ts_code = df['ts_code'][0]
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.execute("delete from weekly_candles where ts_code = :ts_code", {"ts_code": ts_code})
            self.session.bulk_insert_mappings(WeeklyCandle, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()

    def bulk_upsert(self, df):

        for index, candle in df.iterrows():
            obj = get_obj(candle)

            try:
                row = self.session.query(WeeklyCandle).filter(WeeklyCandle.ts_code == candle['ts_code']).filter(
                    WeeklyCandle.trade_date == candle['trade_date']).first()

                if row is None:
                    self.session.add(obj)
                else:
                    if obj.exchange is not None:
                        row.exchange = obj.exchange
                    if obj.open is not None:
                        row.open = obj.open
                    if obj.high is not None:
                        row.high = obj.high
                    if obj.low is not None:
                        row.low = obj.low
                    if obj.close is not None:
                        row.close = obj.close
                    if obj.pre_close is not None:
                        row.pre_close = obj.pre_close
                    if obj.change is not None:
                        row.change = obj.change
                    if obj.pct_chg is not None:
                        row.pct_chg = obj.pct_chg
                    if obj.vol is not None:
                        row.vol = obj.vol
                    if obj.amount is not None:
                        row.amount = obj.amount

            except Exception as e:
                print('Error:', e)

            self.session.commit()
        self.session.close()

        return df
