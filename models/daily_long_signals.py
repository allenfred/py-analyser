from sqlalchemy import Column, Integer, String, Date, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class DailyLongSignal(Base):
    __tablename__ = 'daily_long_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    trade_date = Column(Date)  # 交易日期
    ma20_up = Column(SmallInteger)
    ema20_up = Column(SmallInteger)
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
    ma_gold_cross4 = Column(SmallInteger)
    ema_gold_cross1 = Column(SmallInteger)
    ema_gold_cross2 = Column(SmallInteger)
    ema_gold_cross3 = Column(SmallInteger)
    ema_gold_cross4 = Column(SmallInteger)
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
    bias120 = Column(SmallInteger)

    ma60_support = Column(SmallInteger)
    ema60_support = Column(SmallInteger)
    ma120_support = Column(SmallInteger)
    ema120_support = Column(SmallInteger)

    yearly_price_position = Column(SmallInteger)
    yearly_price_position10 = Column(SmallInteger)
    yearly_price_position20 = Column(SmallInteger)
    yearly_price_position30 = Column(SmallInteger)
    yearly_price_position50 = Column(SmallInteger)
    yearly_price_position70 = Column(SmallInteger)

    ma_group_glue = Column(SmallInteger)
    ema_group_glue = Column(SmallInteger)
    ma_up_arrange51020 = Column(SmallInteger)
    ma_up_arrange5102030 = Column(SmallInteger)
    ma_up_arrange510203060 = Column(SmallInteger)
    ma_up_arrange203060 = Column(SmallInteger)
    ma_up_arrange2060120 = Column(SmallInteger)

    ema_up_arrange51020 = Column(SmallInteger)
    ema_up_arrange5102030 = Column(SmallInteger)
    ema_up_arrange510203060 = Column(SmallInteger)
    ema_up_arrange203060 = Column(SmallInteger)
    ema_up_arrange2055120 = Column(SmallInteger)

    stand_up_ma60 = Column(SmallInteger)
    stand_up_ma120 = Column(SmallInteger)
    stand_up_ema60 = Column(SmallInteger)
    stand_up_ema120 = Column(SmallInteger)

    hammer = Column(SmallInteger)
    pour_hammer = Column(SmallInteger)
    short_end = Column(SmallInteger)
    swallow_up = Column(SmallInteger)
    attack_short = Column(SmallInteger)
    first_light = Column(SmallInteger)
    sunrise = Column(SmallInteger)
    flat_base = Column(SmallInteger)


def get_obj(signal):
    signal = signal.to_dict()
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return DailyLongSignal(
        ts_code=signal.get('ts_code', None),
        trade_date=signal.get('trade_date', None),
        # 技术信号
        ma20_up=signal.get('ma20_up', None),
        ema20_up=signal.get('ema20_up', None),
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
        ma_gold_cross4=signal.get('ma_gold_cross4', None),
        ema_gold_cross1=signal.get('ema_gold_cross1', None),
        ema_gold_cross2=signal.get('ema_gold_cross2', None),
        ema_gold_cross3=signal.get('ema_gold_cross3', None),
        ema_gold_cross4=signal.get('ema_gold_cross4', None),
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
        bias120=signal.get('bias120', None),

        ma60_support=signal.get('ma60_support', None),
        ema60_support=signal.get('ema60_support', None),
        ma120_support=signal.get('ma120_support', None),
        ema120_support=signal.get('ema120_support', None),

        yearly_price_position=signal.get('yearly_price_position', None),
        yearly_price_position10=signal.get('yearly_price_position10', None),
        yearly_price_position20=signal.get('yearly_price_position20', None),
        yearly_price_position30=signal.get('yearly_price_position30', None),
        yearly_price_position50=signal.get('yearly_price_position50', None),
        yearly_price_position70=signal.get('yearly_price_position70', None),

        ma_group_glue=signal.get('ma_group_glue', None),
        ema_group_glue=signal.get('ema_group_glue', None),
        ma_up_arrange51020=signal.get('ma_up_arrange51020', None),
        ma_up_arrange5102030=signal.get('ma_up_arrange5102030', None),
        ma_up_arrange510203060=signal.get('ma_up_arrange510203060', None),
        ma_up_arrange203060=signal.get('ma_up_arrange203060', None),
        ma_up_arrange2060120=signal.get('ma_up_arrange2060120', None),
        ema_up_arrange51020=signal.get('ema_up_arrange51020', None),
        ema_up_arrange5102030=signal.get('ema_up_arrange5102030', None),
        ema_up_arrange510203060=signal.get('ema_up_arrange510203060', None),
        ema_up_arrange203060=signal.get('ema_up_arrange203060', None),
        ema_up_arrange2055120=signal.get('ema_up_arrange2055120', None),

        stand_up_ma60=signal.get('stand_up_ma60', None),
        stand_up_ma120=signal.get('stand_up_ma120', None),
        stand_up_ema60=signal.get('stand_up_ema60', None),
        stand_up_ema120=signal.get('stand_up_ema120', None),

        hammer=signal.get('hammer', None),
        pour_hammer=signal.get('pour_hammer', None),
        short_end=signal.get('short_end', None),
        swallow_up=signal.get('swallow_up', None),
        attack_short=signal.get('attack_short', None),
        first_light=signal.get('first_light', None),
        sunrise=signal.get('sunrise', None),
        flat_base=signal.get('flat_base', None),

    )


class DailyLongSignalDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date from daily_long_signals where ts_code = :ts_code "
                 "order by trade_date desc limit 0,500;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date'])
        self.session.close()

        return df

    def find_all(self, ts_code):
        statement = select(DailyLongSignal).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().all()

        return result

    def add_one(self, signal):
        obj = get_obj(signal)

        rows = self.session.query(DailyLongSignal.id).filter(DailyLongSignal.ts_code == signal['ts_code']).filter(
            DailyLongSignal.trade_date == signal['trade_date']).first()

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
            self.session.bulk_insert_mappings(DailyLongSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def reinsert(self, df, ts_code):
        self.session.execute("delete from daily_long_signals where ts_code = :ts_code", {"ts_code": ts_code})
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(DailyLongSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()
