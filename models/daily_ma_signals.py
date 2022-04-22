from sqlalchemy import Column, Integer, String, Date, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class DailyMaSignal(Base):
    __tablename__ = 'daily_ma_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    trade_date = Column(Date)  # 交易日期
    ma55_first = Column(SmallInteger)
    ma55_second = Column(SmallInteger)
    ma55_third = Column(SmallInteger)
    ma55_fourth = Column(SmallInteger)
    ma55_fifth = Column(SmallInteger)
    ma55_sixth = Column(SmallInteger)
    ma55_seventh = Column(SmallInteger)
    ma55_eighth = Column(SmallInteger)

    ma60_first = Column(SmallInteger)
    ma60_second = Column(SmallInteger)
    ma60_third = Column(SmallInteger)
    ma60_fourth = Column(SmallInteger)
    ma60_fifth = Column(SmallInteger)
    ma60_sixth = Column(SmallInteger)
    ma60_seventh = Column(SmallInteger)
    ma60_eighth = Column(SmallInteger)

    ema55_first = Column(SmallInteger)
    ema55_second = Column(SmallInteger)
    ema55_third = Column(SmallInteger)
    ema55_fourth = Column(SmallInteger)
    ema55_fifth = Column(SmallInteger)
    ema55_sixth = Column(SmallInteger)
    ema55_seventh = Column(SmallInteger)
    ema55_eighth = Column(SmallInteger)

    ema60_first = Column(SmallInteger)
    ema60_second = Column(SmallInteger)
    ema60_third = Column(SmallInteger)
    ema60_fourth = Column(SmallInteger)
    ema60_fifth = Column(SmallInteger)
    ema60_sixth = Column(SmallInteger)
    ema60_seventh = Column(SmallInteger)
    ema60_eighth = Column(SmallInteger)


def get_obj(signal):
    signal = signal.to_dict()
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return DailyMaSignal(
        ts_code=signal.get('ts_code', None),
        trade_date=signal.get('trade_date', None),
        # 技术信号
        ma55_first=signal.get('ma55_first', None),
        ma55_second=signal.get('ma55_second', None),
        ma55_third=signal.get('ma55_third', None),
        ma55_fourth=signal.get('ma55_fourth', None),
        ma55_fifth=signal.get('ma55_fifth', None),
        ma55_sixth=signal.get('ma55_sixth', None),
        ma55_seventh=signal.get('ma55_seventh', None),
        ma55_eighth=signal.get('ma55_eighth', None),

        ma60_first=signal.get('ma60_first', None),
        ma60_second=signal.get('ma60_second', None),
        ma60_third=signal.get('ma60_third', None),
        ma60_fourth=signal.get('ma60_fourth', None),
        ma60_fifth=signal.get('ma60_fifth', None),
        ma60_sixth=signal.get('ma60_sixth', None),
        ma60_seventh=signal.get('ma60_seventh', None),
        ma60_eighth=signal.get('ma60_eighth', None),

        ema55_first=signal.get('ema55_first', None),
        ema55_second=signal.get('ema55_second', None),
        ema55_third=signal.get('ema55_third', None),
        ema55_fourth=signal.get('ema55_fourth', None),
        ema55_fifth=signal.get('ema55_fifth', None),
        ema55_sixth=signal.get('ema55_sixth', None),
        ema55_seventh=signal.get('ema55_seventh', None),
        ema55_eighth=signal.get('ema55_eighth', None),

        ema60_first=signal.get('ema60_first', None),
        ema60_second=signal.get('ema60_second', None),
        ema60_third=signal.get('ema60_third', None),
        ema60_fourth=signal.get('ema60_fourth', None),
        ema60_fifth=signal.get('ema60_fifth', None),
        ema60_sixth=signal.get('ema60_sixth', None),
        ema60_seventh=signal.get('ema60_seventh', None),
        ema60_eighth=signal.get('ema60_eighth', None),
    )


class DailyMaSignalDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date from daily_ma_signals where ts_code = :ts_code "
                 "order by trade_date desc limit 0,500;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date'])
        self.session.close()

        return df

    def find_all(self, ts_code):
        statement = select(DailyMaSignal).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().all()

        return result

    def add_one(self, signal):
        obj = get_obj(signal)

        rows = self.session.query(DailyMaSignal.id).filter(DailyMaSignal.ts_code == signal['ts_code']).filter(
            DailyMaSignal.trade_date == signal['trade_date']).first()

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
            self.session.bulk_insert_mappings(DailyMaSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def reinsert(self, df, ts_code):
        self.session.execute("delete from daily_ma_signals where ts_code = :ts_code", {"ts_code": ts_code})
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(DailyMaSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()
