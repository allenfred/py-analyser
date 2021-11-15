from sqlalchemy import Column, Integer, String, Date, Float, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class DailyIndicator(Base):
    __tablename__ = 'daily_indicators'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    trade_date = Column(Date)  # 交易日期
    ma5 = Column(Float)
    ma10 = Column(Float)
    ma20 = Column(Float)
    ma30 = Column(Float)
    ma34 = Column(Float)
    ma55 = Column(Float)
    ma60 = Column(Float)
    ma120 = Column(Float)
    ma144 = Column(Float)
    ma169 = Column(Float)
    ema5 = Column(Float)
    ema10 = Column(Float)
    ema20 = Column(Float)
    ema30 = Column(Float)
    ema34 = Column(Float)
    ema55 = Column(Float)
    ema60 = Column(Float)
    ema120 = Column(Float)
    ema144 = Column(Float)
    ema169 = Column(Float)
    ma5_slope = Column(Float)
    ma10_slope = Column(Float)
    ma20_slope = Column(Float)
    ma30_slope = Column(Float)
    ma34_slope = Column(Float)
    ma55_slope = Column(Float)
    ma60_slope = Column(Float)
    ma120_slope = Column(Float)
    ma144_slope = Column(Float)
    ma169_slope = Column(Float)
    ema5_slope = Column(Float)
    ema10_slope = Column(Float)
    ema20_slope = Column(Float)
    ema30_slope = Column(Float)
    ema34_slope = Column(Float)
    ema55_slope = Column(Float)
    ema60_slope = Column(Float)
    ema120_slope = Column(Float)
    ema144_slope = Column(Float)
    ema169_slope = Column(Float)
    diff = Column(Float)
    dea = Column(Float)
    macd = Column(Float)
    bias6 = Column(Float)
    bias12 = Column(Float)
    bias24 = Column(Float)
    bias60 = Column(Float)
    bias72 = Column(Float)
    bias120 = Column(Float)
    high_td = Column(Float)
    low_td = Column(Float)


def get_obj(indicator):
    indicator = indicator.to_dict()
    indicator = {k: v if not pd.isna(v) else None for k, v in indicator.items()}

    return DailyIndicator(
        ts_code=indicator.get('ts_code', None),
        trade_date=indicator.get('trade_date', None),
        # 技术指标
        ma5=indicator.get('ma5', None),
        ma10=indicator.get('ma10', None),
        ma20=indicator.get('ma20', None),
        ma30=indicator.get('ma30', None),
        ma34=indicator.get('ma34', None),
        ma55=indicator.get('ma55', None),
        ma60=indicator.get('ma60', None),
        ma120=indicator.get('ma120', None),
        ma144=indicator.get('ma144', None),
        ma169=indicator.get('ma169', None),
        ema5=indicator.get('ema5', None),
        ema10=indicator.get('ema10', None),
        ema20=indicator.get('ema20', None),
        ema30=indicator.get('ema30', None),
        ema34=indicator.get('ema34', None),
        ema55=indicator.get('ema55', None),
        ema60=indicator.get('ema60', None),
        ema120=indicator.get('ema120', None),
        ema144=indicator.get('ema144', None),
        ema169=indicator.get('ema169', None),
        ma5_slope=indicator.get('ma5_slope', None),
        ma10_slope=indicator.get('ma10_slope', None),
        ma20_slope=indicator.get('ma20_slope', None),
        ma30_slope=indicator.get('ma30_slope', None),
        ma34_slope=indicator.get('ma34_slope', None),
        ma55_slope=indicator.get('ma55_slope', None),
        ma60_slope=indicator.get('ma60_slope', None),
        ma120_slope=indicator.get('ma120_slope', None),
        ma144_slope=indicator.get('ma144_slope', None),
        ma169_slope=indicator.get('ma169_slope', None),
        ema5_slope=indicator.get('ema5_slope', None),
        ema10_slope=indicator.get('ema10_slope', None),
        ema20_slope=indicator.get('ema20_slope', None),
        ema30_slope=indicator.get('ema30_slope', None),
        ema34_slope=indicator.get('ema34_slope', None),
        ema55_slope=indicator.get('ema55_slope', None),
        ema60_slope=indicator.get('ema60_slope', None),
        ema120_slope=indicator.get('ema120_slope', None),
        ema144_slope=indicator.get('ema144_slope', None),
        ema169_slope=indicator.get('ema169_slope', None),
        diff=indicator.get('diff', None),
        dea=indicator.get('dea', None),
        macd=indicator.get('macd', None),
        bias6=indicator.get('bias6', None),
        bias12=indicator.get('bias12', None),
        bias24=indicator.get('bias24', None),
        bias60=indicator.get('bias60', None),
        bias72=indicator.get('bias72', None),
        bias120=indicator.get('bias120', None),
        high_td=indicator.get('high_td', None),
        low_td=indicator.get('low_td', None),
    )


class DailyIndicatorDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date from daily_indicators where ts_code = :ts_code "
                 "order by trade_date desc limit 0,500;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date'])
        self.session.close()

        return df

    def find_all_by_ts_code(self, ts_code):
        statement = select(DailyIndicator).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().all()

        return result

    def add_one(self, indicator):
        obj = get_obj(indicator)

        rows = self.session.query(DailyIndicator.id).filter(DailyIndicator.ts_code == indicator['ts_code']).filter(
            DailyIndicator.trade_date == indicator['trade_date']).first()

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

            self.session.bulk_insert_mappings(DailyIndicator, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def reinsert(self, df):
        ts_code = df['ts_code'][0]
        self.session.execute("delete from daily_indicators where ts_code = :ts_code", {"ts_code": ts_code})
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(DailyIndicator, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()