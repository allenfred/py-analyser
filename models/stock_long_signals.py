from sqlalchemy import Column, Integer, String, Date, SmallInteger, select
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class StockLongSignal(Base):
    __tablename__ = 'stock_long_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)
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
    ma_up_ground = Column(SmallInteger)
    ema_up_ground = Column(SmallInteger)
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
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return StockLongSignal(
        ts_code=signal.get('ts_code', None),
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
        ma_up_ground=signal.get('ma_up_ground', None),
        ema_up_ground=signal.get('ema_up_ground', None),
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


class StockLongSignalDao:
    def __init__(self):
        self.session = DBSession()

    def upsert(self, signal):
        obj = get_obj(signal)

        try:
            row = self.session.query(StockLongSignal).filter(StockLongSignal.ts_code == signal['ts_code']).first()

            if row is None:
                self.session.add(obj)
            else:
                if obj.ma20_up is not None:
                    row.ma20_up = obj.ma20_up
                if obj.ema20_up is not None:
                    row.ema20_up = obj.ema20_up
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
                if obj.ma_gold_cross4 is not None:
                    row.ma_gold_cross4 = obj.ma_gold_cross4
                if obj.ema_gold_cross1 is not None:
                    row.ema_gold_cross1 = obj.ema_gold_cross1
                if obj.ema_gold_cross2 is not None:
                    row.ema_gold_cross2 = obj.ema_gold_cross2
                if obj.ema_gold_cross3 is not None:
                    row.ema_gold_cross3 = obj.ema_gold_cross3
                if obj.ema_gold_cross4 is not None:
                    row.ema_gold_cross4 = obj.ema_gold_cross4
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
                if obj.ma_up_ground is not None:
                    row.ma_up_ground = obj.ma_up_ground
                if obj.ema_up_ground is not None:
                    row.ema_up_ground = obj.ema_up_ground
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
                if obj.bias120 is not None:
                    row.bias120 = obj.bias120
                if obj.ma60_support is not None:
                    row.ma60_support = obj.ma60_support
                if obj.ema60_support is not None:
                    row.ema60_support = obj.ema60_support
                if obj.ma120_support is not None:
                    row.ma120_support = obj.ma120_support
                if obj.ema120_support is not None:
                    row.ema120_support = obj.ema120_support
                if obj.yearly_price_position is not None:
                    row.yearly_price_position = obj.yearly_price_position
                if obj.yearly_price_position10 is not None:
                    row.yearly_price_position10 = obj.yearly_price_position10
                if obj.yearly_price_position20 is not None:
                    row.yearly_price_position20 = obj.yearly_price_position20
                if obj.yearly_price_position30 is not None:
                    row.yearly_price_position30 = obj.yearly_price_position30
                if obj.yearly_price_position50 is not None:
                    row.yearly_price_position50 = obj.yearly_price_position50
                if obj.yearly_price_position70 is not None:
                    row.yearly_price_position70 = obj.yearly_price_position70
                if obj.ma_group_glue is not None:
                    row.ma_group_glue = obj.ma_group_glue
                if obj.ema_group_glue is not None:
                    row.ema_group_glue = obj.ema_group_glue
                if obj.ma_up_arrange51020 is not None:
                    row.ma_up_arrange51020 = obj.ma_up_arrange51020
                if obj.ma_up_arrange5102030 is not None:
                    row.ma_up_arrange5102030 = obj.ma_up_arrange5102030
                if obj.ma_up_arrange510203060 is not None:
                    row.ma_up_arrange510203060 = obj.ma_up_arrange510203060
                if obj.ma_up_arrange203060 is not None:
                    row.ma_up_arrange203060 = obj.ma_up_arrange203060
                if obj.ma_up_arrange2060120 is not None:
                    row.ma_up_arrange2060120 = obj.ma_up_arrange2060120
                if obj.ema_up_arrange51020 is not None:
                    row.ema_up_arrange51020 = obj.ema_up_arrange51020
                if obj.ema_up_arrange5102030 is not None:
                    row.ema_up_arrange5102030 = obj.ema_up_arrange5102030
                if obj.ema_up_arrange510203060 is not None:
                    row.ema_up_arrange510203060 = obj.ema_up_arrange510203060
                if obj.ema_up_arrange203060 is not None:
                    row.ema_up_arrange203060 = obj.ema_up_arrange203060
                if obj.ema_up_arrange2055120 is not None:
                    row.ema_up_arrange2055120 = obj.ema_up_arrange2055120
                if obj.stand_up_ma60 is not None:
                    row.stand_up_ma60 = obj.stand_up_ma60
                if obj.stand_up_ma120 is not None:
                    row.stand_up_ma120 = obj.stand_up_ma120
                if obj.stand_up_ema60 is not None:
                    row.stand_up_ema60 = obj.stand_up_ema60
                if obj.stand_up_ema120 is not None:
                    row.stand_up_ema120 = obj.stand_up_ema120
                if obj.hammer is not None:
                    row.hammer = obj.hammer
                if obj.pour_hammer is not None:
                    row.pour_hammer = obj.pour_hammer
                if obj.short_end is not None:
                    row.short_end = obj.short_end
                if obj.swallow_up is not None:
                    row.swallow_up = obj.swallow_up
                if obj.attack_short is not None:
                    row.attack_short = obj.attack_short
                if obj.first_light is not None:
                    row.first_light = obj.first_light
                if obj.sunrise is not None:
                    row.sunrise = obj.sunrise
                if obj.flat_base is not None:
                    row.flat_base = obj.flat_base

        except Exception as e:
            print('Error:', e)

        self.session.commit()
        self.session.close()

