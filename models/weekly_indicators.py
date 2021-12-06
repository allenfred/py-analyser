from sqlalchemy import Column, Integer, String, Date, Float, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class WeeklyIndicator(Base):
    __tablename__ = 'weekly_indicators'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    trade_date = Column(Date)  # 交易日期
    ma5 = Column(Float)
    ma10 = Column(Float)
    ma20 = Column(Float)
    ma30 = Column(Float)
    ma60 = Column(Float)
    ema5 = Column(Float)
    ema10 = Column(Float)
    ema20 = Column(Float)
    ema30 = Column(Float)
    ema60 = Column(Float)
    diff = Column(Float)
    dea = Column(Float)
    macd = Column(Float)


def get_obj(indicator):
    indicator = indicator.to_dict()
    indicator = {k: v if not pd.isna(v) else None for k, v in indicator.items()}

    return WeeklyIndicator(
        ts_code=indicator.get('ts_code', None),
        trade_date=indicator.get('trade_date', None),
        # 技术指标
        ma5=candle.get('ma5', None),
        ma10=candle.get('ma10', None),
        ma20=candle.get('ma20', None),
        ma30=candle.get('ma30', None),
        ma60=candle.get('ma60', None),
        ema5=candle.get('ema5', None),
        ema10=candle.get('ema10', None),
        ema20=candle.get('ema20', None),
        ema30=candle.get('ema30', None),
        ema60=candle.get('ema60', None),
        diff=candle.get('diff', None),
        dea=candle.get('dea', None),
        macd=candle.get('macd', None)
    )


class WeeklyIndicatorDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date from weekly_indicators where ts_code = :ts_code "
                 "order by trade_date desc limit 0,500;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date'])
        self.session.close()

        return df

    def find_all_by_ts_code(self, ts_code):
        statement = select(WeeklyIndicator).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().all()

        return result

    def add_one(self, indicator):
        obj = get_obj(indicator)

        rows = self.session.query(WeeklyIndicator.id).filter(WeeklyIndicator.ts_code == indicator['ts_code']).filter(
            WeeklyIndicator.trade_date == indicator['trade_date']).first()

        if len(rows) == 0:
            self.session.add(obj)

        self.session.commit()
        self.session.close()

        return obj

    def bulk_insert(self, df, ts_code):
        db_df = self.find_by_ts_code(ts_code)
        insert_needed_df = df.loc[~df["trade_date"].isin(db_df["trade_date"].to_numpy())]

        items = []
        for index, item in insert_needed_df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:

            self.session.bulk_insert_mappings(WeeklyIndicator, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def reinsert(self, df):
        ts_code = df['ts_code'][0]
        self.session.execute("delete from weekly_indicators where ts_code = :ts_code", {"ts_code": ts_code})
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(WeeklyIndicator, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()