from sqlalchemy import Column, Integer, String, Date, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class DailyShortSignal(Base):
    __tablename__ = 'daily_short_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    trade_date = Column(Date)  # 交易日期
    # 技术信号
    ma30_up = Column(SmallInteger)
    ema30_up = Column(SmallInteger)
    ma60_up = Column(SmallInteger)
    ema60_up = Column(SmallInteger)
    ma120_up = Column(SmallInteger)
    ema120_up = Column(SmallInteger)
    ma_arrange = Column(SmallInteger)
    ema_arrange = Column(SmallInteger)
    short_ma_arrange1 = Column(SmallInteger)
    short_ma_arrange2 = Column(SmallInteger)
    short_ema_arrange1 = Column(SmallInteger)
    short_ema_arrange2 = Column(SmallInteger)
    middle_ma_arrange1 = Column(SmallInteger)
    middle_ma_arrange2 = Column(SmallInteger)
    middle_ema_arrange1 = Column(SmallInteger)
    middle_ema_arrange2 = Column(SmallInteger)
    long_ma_arrange1 = Column(SmallInteger)
    long_ma_arrange2 = Column(SmallInteger)
    long_ema_arrange1 = Column(SmallInteger)
    long_ema_arrange2 = Column(SmallInteger)
    ma_gold_cross1 = Column(SmallInteger)
    ma_gold_cross2 = Column(SmallInteger)
    ma_gold_cross3 = Column(SmallInteger)
    ema_gold_cross1 = Column(SmallInteger)
    ema_gold_cross2 = Column(SmallInteger)
    ema_gold_cross3 = Column(SmallInteger)
    ma_silver_valley = Column(SmallInteger)
    ema_silver_valley = Column(SmallInteger)
    ma_gold_valley = Column(SmallInteger)
    ema_gold_valley = Column(SmallInteger)
    ma_out_sea = Column(SmallInteger)
    ema_out_sea = Column(SmallInteger)
    ma_hold_moon = Column(SmallInteger)
    ema_hold_moon = Column(SmallInteger)
    ma_over_gate = Column(SmallInteger)
    ema_over_gate = Column(SmallInteger)
    ma_up_group = Column(SmallInteger)
    ema_up_group = Column(SmallInteger)
    ma_spider = Column(SmallInteger)
    ma_spider2 = Column(SmallInteger)
    ema_spider = Column(SmallInteger)
    ema_spider2 = Column(SmallInteger)
    td8 = Column(SmallInteger)
    td9 = Column(SmallInteger)
    bias6 = Column(SmallInteger)
    bias12 = Column(SmallInteger)
    bias24 = Column(SmallInteger)
    bias60 = Column(SmallInteger)
    bias72 = Column(SmallInteger)


def get_obj(signal):
    signal = signal.to_dict()
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return DailyLongSignal(
        ts_code=signal.get('ts_code', None),
        trade_date=signal.get('trade_date', None),
        # 技术信号
        ma30_up=signal.get('ma30_up', None),
        ema30_up=signal.get('ema30_up', None),
        ma60_up=signal.get('ma60_up', None),
        ema60_up=signal.get('ema60_up', None),
        ma120_up=signal.get('ma120_up', None),
        ema120_up=signal.get('ema120_up', None),
        ma_arrange=signal.get('ma_arrange', None),
        ema_arrange=signal.get('ema_arrange', None),
        short_ma_arrange1=signal.get('short_ma_arrange1', None),
        short_ma_arrange2=signal.get('short_ma_arrange2', None),
        short_ema_arrange1=signal.get('short_ema_arrange1', None),
        short_ema_arrange2=signal.get('short_ema_arrange2', None),
        middle_ma_arrange1=signal.get('middle_ma_arrange1', None),
        middle_ma_arrange2=signal.get('middle_ma_arrange2', None),
        middle_ema_arrange1=signal.get('middle_ema_arrange1', None),
        middle_ema_arrange2=signal.get('middle_ema_arrange2', None),
        long_ma_arrange1=signal.get('long_ma_arrange1', None),
        long_ma_arrange2=signal.get('long_ma_arrange2', None),
        long_ema_arrange1=signal.get('long_ema_arrange1', None),
        long_ema_arrange2=signal.get('long_ema_arrange2', None),
        ma_gold_cross1=signal.get('ma_gold_cross1', None),
        ma_gold_cross2=signal.get('ma_gold_cross2', None),
        ma_gold_cross3=signal.get('ma_gold_cross3', None),
        ema_gold_cross1=signal.get('ema_gold_cross1', None),
        ema_gold_cross2=signal.get('ema_gold_cross2', None),
        ema_gold_cross3=signal.get('ema_gold_cross3', None),
        ma_silver_valley=signal.get('ma_silver_valley', None),
        ema_silver_valley=signal.get('ema_silver_valley', None),
        ma_gold_valley=signal.get('ma_gold_valley', None),
        ema_gold_valley=signal.get('ema_gold_valley', None),
        ma_out_sea=signal.get('ma_out_sea', None),
        ema_out_sea=signal.get('ema_out_sea', None),
        ma_hold_moon=signal.get('ma_hold_moon', None),
        ema_hold_moon=signal.get('ema_hold_moon', None),
        ma_over_gate=signal.get('ma_over_gate', None),
        ema_over_gate=signal.get('ema_over_gate', None),
        ma_up_group=signal.get('ma_up_group', None),
        ema_up_group=signal.get('ema_up_group', None),
        ma_spider=signal.get('ma_spider', None),
        ma_spider2=signal.get('ma_spider2', None),
        ema_spider=signal.get('ema_spider', None),
        ema_spider2=signal.get('ema_spider2', None),
        td8=signal.get('td8', None),
        td9=signal.get('td9', None),
        bias6=signal.get('bias6', None),
        bias12=signal.get('bias12', None),
        bias24=signal.get('bias24', None),
        bias60=signal.get('bias60', None),
        bias72=signal.get('bias72', None),
    )


class DailyShortSignalDao:
    def __init__(self):
        self.session = DBSession()

    def find_all(self, ts_code):
        statement = select(DailyShortSignal).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().all()

        return result

    def add_one(self, signal):
        obj = get_obj(signal)

        rows = self.session.query(DailyShortSignal.id).filter(DailyShortSignal.ts_code == signal['ts_code']).filter(
            DailyShortSignal.trade_date == signal['trade_date']).first()

        if len(rows) == 0:
            self.session.add(obj)

        self.session.commit()
        self.session.close()

        return obj

    def bulk_insert(self, df):
        items = []
        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:

            self.session.bulk_insert_mappings(DailyShortSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def bulk_upsert(self, df):
        for index, signal in df.iterrows():
            obj = get_obj(signal)
            try:
                row = self.session.query(DailyShortSignal).filter(DailyShortSignal.ts_code == signal['ts_code']).filter(
                    DailyShortSignal.trade_date == signal['trade_date']).first()

                if row is None:
                    self.session.add(obj)
                else:
                    if obj.ma30_up is not None:
                        row.ma30_up = obj.ma30_up
                    if obj.ema30_up is not None:
                        row.ema30_up = obj.ema30_up
                    if obj.ma60_up is not None:
                        row.ma60_up = obj.ma60_up
                    if obj.ema60_up is not None:
                        row.ema60_up = obj.ema60_up
                    if obj.ma120_up is not None:
                        row.ma120_up = obj.ma120_up
                    if obj.ema120_up is not None:
                        row.ema120_up = obj.ema120_up
                    if obj.ma_arrange is not None:
                        row.ma_arrange = obj.ma_arrange
                    if obj.ema_arrange is not None:
                        row.ema_arrange = obj.ema_arrange
                    if obj.short_ma_arrange1 is not None:
                        row.short_ma_arrange1 = obj.short_ma_arrange1
                    if obj.short_ma_arrange2 is not None:
                        row.short_ma_arrange2 = obj.short_ma_arrange2
                    if obj.short_ema_arrange1 is not None:
                        row.short_ema_arrange1 = obj.short_ema_arrange1
                    if obj.short_ema_arrange2 is not None:
                        row.short_ema_arrange2 = obj.short_ema_arrange2
                    if obj.middle_ma_arrange1 is not None:
                        row.middle_ma_arrange1 = obj.middle_ma_arrange1
                    if obj.middle_ma_arrange2 is not None:
                        row.middle_ma_arrange2 = obj.middle_ma_arrange2
                    if obj.middle_ema_arrange1 is not None:
                        row.middle_ema_arrange1 = obj.middle_ema_arrange1
                    if obj.middle_ema_arrange2 is not None:
                        row.middle_ema_arrange2 = obj.middle_ema_arrange2
                    if obj.long_ma_arrange1 is not None:
                        row.long_ma_arrange1 = obj.long_ma_arrange1
                    if obj.long_ma_arrange2 is not None:
                        row.long_ma_arrange2 = obj.long_ma_arrange2
                    if obj.long_ema_arrange1 is not None:
                        row.long_ema_arrange1 = obj.long_ema_arrange1
                    if obj.long_ema_arrange2 is not None:
                        row.long_ema_arrange2 = obj.long_ema_arrange2
                    if obj.ma_gold_cross1 is not None:
                        row.ma_gold_cross1 = obj.ma_gold_cross1
                    if obj.ma_gold_cross2 is not None:
                        row.ma_gold_cross2 = obj.ma_gold_cross2
                    if obj.ma_gold_cross3 is not None:
                        row.ma_gold_cross3 = obj.ma_gold_cross3
                    if obj.ema_gold_cross1 is not None:
                        row.ema_gold_cross1 = obj.ema_gold_cross1
                    if obj.ema_gold_cross2 is not None:
                        row.ema_gold_cross2 = obj.ema_gold_cross2
                    if obj.ema_gold_cross3 is not None:
                        row.ema_gold_cross3 = obj.ema_gold_cross3
                    if obj.ma_silver_valley is not None:
                        row.ma_silver_valley = obj.ma_silver_valley
                    if obj.ema_silver_valley is not None:
                        row.ema_silver_valley = obj.ema_silver_valley
                    if obj.ma_gold_valley is not None:
                        row.ma_gold_valley = obj.ma_gold_valley
                    if obj.ema_gold_valley is not None:
                        row.ema_gold_valley = obj.ema_gold_valley
                    if obj.ma_out_sea is not None:
                        row.ma_out_sea = obj.ma_out_sea
                    if obj.ema_out_sea is not None:
                        row.ema_out_sea = obj.ema_out_sea
                    if obj.ma_hold_moon is not None:
                        row.ma_hold_moon = obj.ma_hold_moon
                    if obj.ema_hold_moon is not None:
                        row.ema_hold_moon = obj.ema_hold_moon
                    if obj.ma_over_gate is not None:
                        row.ma_over_gate = obj.ma_over_gate
                    if obj.ema_over_gate is not None:
                        row.ema_over_gate = obj.ema_over_gate
                    if obj.ma_up_group is not None:
                        row.ma_up_group = obj.ma_up_group
                    if obj.ema_up_group is not None:
                        row.ema_up_group = obj.ema_up_group
                    if obj.ma_spider is not None:
                        row.ma_spider = obj.ma_spider
                    if obj.ma_spider2 is not None:
                        row.ma_spider2 = obj.ma_spider2
                    if obj.ema_spider is not None:
                        row.ema_spider = obj.ema_spider
                    if obj.ema_spider2 is not None:
                        row.ema_spider2 = obj.ema_spider2
                    if obj.td8 is not None:
                        row.td8 = obj.td8
                    if obj.td9 is not None:
                        row.td9 = obj.td9
                    if obj.bias6 is not None:
                        row.bias6 = obj.bias6
                    if obj.bias12 is not None:
                        row.bias12 = obj.bias12
                    if obj.bias24 is not None:
                        row.bias24 = obj.bias24
                    if obj.bias60 is not None:
                        row.bias60 = obj.bias60
                    if obj.bias72 is not None:
                        row.bias72 = obj.bias72

            except Exception as e:
                print('Error:', e)

            self.session.commit()
        self.session.close()

        return df

    def reset_insert(self, df):
        ts_code = df['ts_code'][0]
        self.session.execute("delete from daily_short_signals where ts_code = :ts_code", {"ts_code": ts_code})
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(DailyShortSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()
