from sqlalchemy import Column, Integer, String, Date, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class DailyKlineSignal(Base):
    __tablename__ = 'daily_kline_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    trade_date = Column(Date)  # 交易日期
    hammer = Column(SmallInteger)
    pour_hammer = Column(SmallInteger)
    long_end = Column(SmallInteger)
    short_end = Column(SmallInteger)
    swallow_up = Column(SmallInteger)
    swallow_down = Column(SmallInteger)
    attack_short = Column(SmallInteger)
    first_light = Column(SmallInteger)
    sunrise = Column(SmallInteger)
    flat_base = Column(SmallInteger)
    hang_neck = Column(SmallInteger)
    shooting = Column(SmallInteger)
    rise_line = Column(SmallInteger)
    jump_line = Column(SmallInteger)
    up_screw = Column(SmallInteger)
    down_screw = Column(SmallInteger)


def get_obj(signal):
    signal = signal.to_dict()
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return DailyKlineSignal(
        ts_code=signal.get('ts_code', None),
        trade_date=signal.get('trade_date', None),
        hammer=signal.get('hammer', None),
        pour_hammer=signal.get('pour_hammer', None),
        long_end=signal.get('long_end', None),
        short_end=signal.get('short_end', None),
        swallow_up=signal.get('swallow_up', None),
        swallow_down=signal.get('swallow_down', None),
        attack_short=signal.get('attack_short', None),
        first_light=signal.get('first_light', None),
        sunrise=signal.get('sunrise', None),
        flat_base=signal.get('flat_base', None),
        hang_neck=signal.get('hang_neck', None),
        shooting=signal.get('shooting', None),
        rise_line=signal.get('rise_line', None),
        jump_line=signal.get('jump_line', None),
        up_screw=signal.get('up_screw', None),
        down_screw=signal.get('down_screw', None),
    )


class DailyKlineSignalDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date from daily_kline_signals where ts_code = :ts_code "
                 "order by trade_date desc limit 0,500;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date'])
        self.session.close()

        return df

    def find_all(self, ts_code):
        statement = select(DailyKlineSignal).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().all()

        return result

    def add_one(self, signal):
        obj = get_obj(signal)

        rows = self.session.query(DailyKlineSignal.id).filter(DailyKlineSignal.ts_code == signal['ts_code']).filter(
            DailyKlineSignal.trade_date == signal['trade_date']).first()

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
            self.session.bulk_insert_mappings(DailyKlineSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def reinsert(self, df, ts_code):
        self.session.execute("delete from daily_kline_signals where ts_code = :ts_code", {"ts_code": ts_code})
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(DailyKlineSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()
