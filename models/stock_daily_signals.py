from sqlalchemy import Column, Integer, String, Date, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class StockDailySignal(Base):
    __tablename__ = 'stock_daily_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)
    trade_date = Column(Date)  # 交易日期
    exchange = Column(String)  # 交易所代码

    ma20_up = Column(SmallInteger)
    ema20_up = Column(SmallInteger)
    ma30_up = Column(SmallInteger)
    ema30_up = Column(SmallInteger)
    ma60_up = Column(SmallInteger)
    ema60_up = Column(SmallInteger)
    ma120_up = Column(SmallInteger)
    ema120_up = Column(SmallInteger)
    ma20_down = Column(SmallInteger)
    ema20_down = Column(SmallInteger)
    ma30_down = Column(SmallInteger)
    ema30_down = Column(SmallInteger)
    ma60_down = Column(SmallInteger)
    ema60_down = Column(SmallInteger)
    ma120_down = Column(SmallInteger)
    ema120_down = Column(SmallInteger)

    up_ma_arrange = Column(SmallInteger)
    up_ema_arrange = Column(SmallInteger)
    down_ma_arrange = Column(SmallInteger)
    down_ema_arrange = Column(SmallInteger)

    up_short_ma_arrange1 = Column(SmallInteger)
    up_short_ma_arrange2 = Column(SmallInteger)
    up_short_ema_arrange1 = Column(SmallInteger)
    up_short_ema_arrange2 = Column(SmallInteger)
    up_middle_ma_arrange1 = Column(SmallInteger)
    up_middle_ma_arrange2 = Column(SmallInteger)
    up_middle_ema_arrange1 = Column(SmallInteger)
    up_middle_ema_arrange2 = Column(SmallInteger)
    up_long_ma_arrange1 = Column(SmallInteger)
    up_long_ma_arrange2 = Column(SmallInteger)
    up_long_ema_arrange1 = Column(SmallInteger)
    up_long_ema_arrange2 = Column(SmallInteger)

    down_short_ma_arrange1 = Column(SmallInteger)
    down_short_ma_arrange2 = Column(SmallInteger)
    down_short_ema_arrange1 = Column(SmallInteger)
    down_short_ema_arrange2 = Column(SmallInteger)
    down_middle_ma_arrange1 = Column(SmallInteger)
    down_middle_ma_arrange2 = Column(SmallInteger)
    down_middle_ema_arrange1 = Column(SmallInteger)
    down_middle_ema_arrange2 = Column(SmallInteger)
    down_long_ma_arrange1 = Column(SmallInteger)
    down_long_ma_arrange2 = Column(SmallInteger)
    down_long_ema_arrange1 = Column(SmallInteger)
    down_long_ema_arrange2 = Column(SmallInteger)

    ma_gold_cross1 = Column(SmallInteger)
    ma_gold_cross2 = Column(SmallInteger)
    ma_gold_cross3 = Column(SmallInteger)
    ma_gold_cross4 = Column(SmallInteger)

    ma_dead_cross1 = Column(SmallInteger)
    ma_dead_cross2 = Column(SmallInteger)
    ma_dead_cross3 = Column(SmallInteger)

    ma_silver_valley = Column(SmallInteger)
    ma_gold_valley = Column(SmallInteger)
    ma_out_sea = Column(SmallInteger)
    ma_hold_moon = Column(SmallInteger)
    ma_over_gate = Column(SmallInteger)
    ma_up_ground = Column(SmallInteger)

    ma_dead_valley = Column(SmallInteger)
    ma_knife = Column(SmallInteger)
    ma_dark_cloud = Column(SmallInteger)
    ma_set_sail = Column(SmallInteger)
    ma_supreme = Column(SmallInteger)
    ma_dead_jump = Column(SmallInteger)

    up_ma_spider = Column(SmallInteger)
    down_ma_spider = Column(SmallInteger)

    up_hill = Column(SmallInteger)
    down_hill = Column(SmallInteger)

    up_wave = Column(SmallInteger)
    limit_up_gene = Column(SmallInteger)

    up_td8 = Column(SmallInteger)
    up_td9 = Column(SmallInteger)

    down_td8 = Column(SmallInteger)
    down_td9 = Column(SmallInteger)

    up_bias6 = Column(SmallInteger)  # 正乖离(超买)
    up_bias12 = Column(SmallInteger)
    up_bias24 = Column(SmallInteger)
    up_bias60 = Column(SmallInteger)
    up_bias72 = Column(SmallInteger)
    up_bias120 = Column(SmallInteger)

    down_bias6 = Column(SmallInteger)  # 负乖离(超卖)
    down_bias12 = Column(SmallInteger)
    down_bias24 = Column(SmallInteger)
    down_bias60 = Column(SmallInteger)
    down_bias72 = Column(SmallInteger)
    down_bias120 = Column(SmallInteger)

    ma60_support = Column(SmallInteger)
    ma120_support = Column(SmallInteger)

    ma_glue = Column(SmallInteger)
    ema_glue = Column(SmallInteger)

    stand_up_ma60 = Column(SmallInteger)
    stand_up_ma120 = Column(SmallInteger)

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
    drop_line = Column(SmallInteger)
    up_screw = Column(SmallInteger)
    down_screw = Column(SmallInteger)
    down_rise = Column(SmallInteger)

    upward_jump = Column(SmallInteger)
    downward_jump = Column(SmallInteger)
    rise_limit = Column(SmallInteger)
    drop_limit = Column(SmallInteger)
    up_cross3ma = Column(SmallInteger)
    up_cross4ma = Column(SmallInteger)
    drop_cross3ma = Column(SmallInteger)
    drop_cross4ma = Column(SmallInteger)

    ma60_first = Column(SmallInteger)
    ma60_second = Column(SmallInteger)
    ma60_third = Column(SmallInteger)
    ma60_fourth = Column(SmallInteger)
    ma60_fifth = Column(SmallInteger)
    ma60_sixth = Column(SmallInteger)
    ma60_seventh = Column(SmallInteger)
    ma60_eighth = Column(SmallInteger)

    ma_rule_marker = Column(SmallInteger)

    max_vol = Column(SmallInteger)
    huge_vol = Column(SmallInteger)
    large_vol = Column(SmallInteger)
    high_vol = Column(SmallInteger)
    common_vol = Column(SmallInteger)
    low_vol = Column(SmallInteger)
    increase_vol = Column(SmallInteger)
    decrease_vol = Column(SmallInteger)
    increasingly_vol = Column(SmallInteger)
    decreasingly_vol = Column(SmallInteger)

    hlines = Column(String)
    limit_pullback = Column(SmallInteger)
    up_pullback = Column(SmallInteger)
    down_pullback = Column(SmallInteger)
    up_break = Column(SmallInteger)
    down_break = Column(SmallInteger)
    hline_support = Column(SmallInteger)
    hline_resistance = Column(SmallInteger)


def get_obj(signal):
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return StockDailySignal(
        ts_code=signal.get('ts_code', None),
        trade_date=signal.get('trade_date', None),
        exchange=signal.get('exchange', None),

        ma20_up=signal.get('ma20_up', None),
        ema20_up=signal.get('ema20_up', None),
        ma30_up=signal.get('ma30_up', None),
        ema30_up=signal.get('ema30_up', None),
        ma60_up=signal.get('ma60_up', None),
        ema60_up=signal.get('ema60_up', None),
        ma120_up=signal.get('ma120_up', None),
        ema120_up=signal.get('ema120_up', None),

        ma20_down=signal.get('ma20_down', None),
        ema20_down=signal.get('ema20_down', None),
        ma30_down=signal.get('ma30_down', None),
        ema30_down=signal.get('ema30_down', None),
        ma60_down=signal.get('ma60_down', None),
        ema60_down=signal.get('ema60_down', None),
        ma120_down=signal.get('ma120_down', None),
        ema120_down=signal.get('ema120_down', None),

        up_ma_arrange=signal.get('up_ma_arrange', None),
        up_ema_arrange=signal.get('up_ema_arrange', None),
        down_ma_arrange=signal.get('down_ma_arrange', None),
        down_ema_arrange=signal.get('down_ema_arrange', None),

        up_short_ma_arrange1=signal.get('up_short_ma_arrange1', None),
        up_short_ma_arrange2=signal.get('up_short_ma_arrange2', None),
        up_short_ema_arrange1=signal.get('up_short_ema_arrange1', None),
        up_short_ema_arrange2=signal.get('up_short_ema_arrange2', None),
        up_middle_ma_arrange1=signal.get('up_middle_ma_arrange1', None),
        up_middle_ma_arrange2=signal.get('up_middle_ma_arrange2', None),
        up_middle_ema_arrange1=signal.get('up_middle_ema_arrange1', None),
        up_middle_ema_arrange2=signal.get('up_middle_ema_arrange2', None),
        up_long_ma_arrange1=signal.get('up_long_ma_arrange1', None),
        up_long_ma_arrange2=signal.get('up_long_ma_arrange2', None),
        up_long_ema_arrange1=signal.get('up_long_ema_arrange1', None),
        up_long_ema_arrange2=signal.get('up_long_ema_arrange2', None),

        down_short_ma_arrange1=signal.get('down_short_ma_arrange1', None),
        down_short_ma_arrange2=signal.get('down_short_ma_arrange2', None),
        down_short_ema_arrange1=signal.get('down_short_ema_arrange1', None),
        down_short_ema_arrange2=signal.get('down_short_ema_arrange2', None),
        down_middle_ma_arrange1=signal.get('down_middle_ma_arrange1', None),
        down_middle_ma_arrange2=signal.get('down_middle_ma_arrange2', None),
        down_middle_ema_arrange1=signal.get('down_middle_ema_arrange1', None),
        down_middle_ema_arrange2=signal.get('down_middle_ema_arrange2', None),
        down_long_ma_arrange1=signal.get('down_long_ma_arrange1', None),
        down_long_ma_arrange2=signal.get('down_long_ma_arrange2', None),
        down_long_ema_arrange1=signal.get('down_long_ema_arrange1', None),
        down_long_ema_arrange2=signal.get('down_long_ema_arrange2', None),

        ma_gold_cross1=signal.get('ma_gold_cross1', None),
        ma_gold_cross2=signal.get('ma_gold_cross2', None),
        ma_gold_cross3=signal.get('ma_gold_cross3', None),
        ma_gold_cross4=signal.get('ma_gold_cross4', None),

        ma_dead_cross1=signal.get('ma_dead_cross1', None),
        ma_dead_cross2=signal.get('ma_dead_cross2', None),
        ma_dead_cross3=signal.get('ma_dead_cross3', None),

        ma_silver_valley=signal.get('ma_silver_valley', None),
        ma_gold_valley=signal.get('ma_gold_valley', None),
        ma_dead_valley=signal.get('ma_dead_valley', None),

        ma_out_sea=signal.get('ma_out_sea', None),
        ma_hold_moon=signal.get('ma_hold_moon', None),
        ma_over_gate=signal.get('ma_over_gate', None),
        ma_up_ground=signal.get('ma_up_ground', None),

        ma_knife=signal.get('ma_knife', None),
        ma_dark_cloud=signal.get('ma_dark_cloud', None),
        ma_set_sail=signal.get('ma_set_sail', None),
        ma_supreme=signal.get('ma_supreme', None),
        ma_dead_jump=signal.get('ma_dead_jump', None),

        up_ma_spider=signal.get('up_ma_spider', None),
        down_ma_spider=signal.get('down_ma_spider', None),

        up_hill=signal.get('up_hill', None),
        down_hill=signal.get('down_hill', None),

        up_wave=signal.get('up_wave', None),
        limit_up_gene=signal.get('limit_up_gene', None),

        up_td8=signal.get('up_td8', None),
        up_td9=signal.get('up_td9', None),

        down_td8=signal.get('down_td8', None),
        down_td9=signal.get('down_td9', None),

        up_bias6=signal.get('up_bias6', None),
        up_bias12=signal.get('up_bias12', None),
        up_bias24=signal.get('up_bias24', None),
        up_bias60=signal.get('up_bias60', None),
        up_bias72=signal.get('up_bias72', None),
        up_bias120=signal.get('up_bias120', None),

        down_bias6=signal.get('down_bias6', None),
        down_bias12=signal.get('down_bias12', None),
        down_bias24=signal.get('down_bias24', None),
        down_bias60=signal.get('down_bias60', None),
        down_bias72=signal.get('down_bias72', None),
        down_bias120=signal.get('down_bias120', None),

        ma60_support=signal.get('ma60_support', None),
        ma120_support=signal.get('ma120_support', None),

        ma_glue=signal.get('ma_glue', None),

        stand_up_ma60=signal.get('stand_up_ma60', None),
        stand_up_ma120=signal.get('stand_up_ma120', None),

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
        drop_line=signal.get('drop_line', None),
        up_screw=signal.get('up_screw', None),
        down_screw=signal.get('down_screw', None),
        down_rise=signal.get('down_rise', None),

        upward_jump=signal.get('upward_jump', None),
        downward_jump=signal.get('downward_jump', None),
        rise_limit=signal.get('rise_limit', None),
        drop_limit=signal.get('drop_limit', None),
        up_cross3ma=signal.get('up_cross3ma', None),
        up_cross4ma=signal.get('up_cross4ma', None),
        drop_cross3ma=signal.get('drop_cross3ma', None),
        drop_cross4ma=signal.get('drop_cross4ma', None),

        ma60_first=signal.get('ma60_first', None),
        ma60_second=signal.get('ma60_second', None),
        ma60_third=signal.get('ma60_third', None),
        ma60_fourth=signal.get('ma60_fourth', None),
        ma60_fifth=signal.get('ma60_fifth', None),
        ma60_sixth=signal.get('ma60_sixth', None),
        ma60_seventh=signal.get('ma60_seventh', None),
        ma60_eighth=signal.get('ma60_eighth', None),

        ma_rule_marker=signal.get('ma_rule_marker', None),

        max_vol=signal.get('max_vol', None),
        huge_vol=signal.get('huge_vol', None),
        large_vol=signal.get('large_vol', None),
        high_vol=signal.get('high_vol', None),
        common_vol=signal.get('common_vol', None),
        low_vol=signal.get('low_vol', None),
        increase_vol=signal.get('increase_vol', None),
        decrease_vol=signal.get('decrease_vol', None),
        increasingly_vol=signal.get('increasingly_vol', None),
        decreasingly_vol=signal.get('decreasingly_vol', None),

        hlines=signal.get('hlines', None),
        limit_pullback=signal.get('limit_pullback', None),
        up_pullback=signal.get('up_pullback', None),
        down_pullback=signal.get('down_pullback', None),
        up_break=signal.get('up_break', None),
        down_break=signal.get('down_break', None),
        hline_support=signal.get('hline_support', None),
        hline_resistance=signal.get('hline_resistance', None),
    )


class StockDailySignalDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date from stock_daily_signals where ts_code = :ts_code "
                 "order by trade_date desc limit 0,20;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date'])
        self.session.close()

        return df

    def find_all(self, ts_code):
        statement = select(StockDailySignal).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().all()

        return result

    def bulk_insert(self, df, ts_code):
        db_df = self.find_by_ts_code(ts_code)
        insert_needed_df = df.loc[~df["trade_date"].isin(db_df["trade_date"].to_numpy())]

        items = []
        for index, item in insert_needed_df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(StockDailySignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def reinsert(self, df, ts_code):
        trade_date = df['trade_date'].to_numpy()[0]

        self.session.execute("delete from stock_daily_signals where "
                             "ts_code = :ts_code and trade_date >= :trade_date;",
                             {"ts_code": ts_code, "trade_date": trade_date})
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(StockDailySignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()

    def upsert(self, signal):
        if signal['ma60_first'] == 1 or signal['ma60_second'] == 1 or signal['ma60_third'] == 1 or \
                signal['ma60_fourth'] == 1 or signal['ma60_fifth'] == 1 or signal['ma60_sixth'] == 1 or \
                signal['ma60_seventh'] == 1 or signal['ma60_eighth'] == 1:
            signal['ma_rule_marker'] = 1

        obj = get_obj(signal)

        try:
            row = self.session.query(StockDailySignal).filter(StockDailySignal.ts_code == signal['ts_code'],
                                                              StockDailySignal.trade_date == signal[
                                                                  'trade_date']).first()

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

                if obj.ma20_down is not None:
                    row.ma20_down = obj.ma20_down
                if obj.ema20_down is not None:
                    row.ema20_down = obj.ema20_down
                if obj.ma30_down is not None:
                    row.ma30_down = obj.ma30_down
                if obj.ema30_down is not None:
                    row.ema30_down = obj.ema30_down
                if obj.ma60_down is not None:
                    row.ma60_down = obj.ma60_down
                if obj.ema60_down is not None:
                    row.ema60_down = obj.ema60_down
                if obj.ma120_down is not None:
                    row.ma120_down = obj.ma120_down
                if obj.ema120_down is not None:
                    row.ema120_down = obj.ema120_down

                if obj.up_ma_arrange is not None:
                    row.up_ma_arrange = obj.up_ma_arrange
                if obj.up_ema_arrange is not None:
                    row.up_ema_arrange = obj.up_ema_arrange
                if obj.down_ma_arrange is not None:
                    row.down_ma_arrange = obj.down_ma_arrange
                if obj.down_ema_arrange is not None:
                    row.down_ema_arrange = obj.down_ema_arrange

                if obj.up_short_ma_arrange1 is not None:
                    row.up_short_ma_arrange1 = obj.up_short_ma_arrange1
                if obj.up_short_ma_arrange2 is not None:
                    row.up_short_ma_arrange2 = obj.up_short_ma_arrange2
                if obj.up_short_ema_arrange1 is not None:
                    row.up_short_ema_arrange1 = obj.up_short_ema_arrange1
                if obj.up_short_ema_arrange2 is not None:
                    row.up_short_ema_arrange2 = obj.up_short_ema_arrange2
                if obj.up_middle_ma_arrange1 is not None:
                    row.up_middle_ma_arrange1 = obj.up_middle_ma_arrange1
                if obj.up_middle_ma_arrange2 is not None:
                    row.up_middle_ma_arrange2 = obj.up_middle_ma_arrange2
                if obj.up_middle_ema_arrange1 is not None:
                    row.up_middle_ema_arrange1 = obj.up_middle_ema_arrange1
                if obj.up_middle_ema_arrange2 is not None:
                    row.up_middle_ema_arrange2 = obj.up_middle_ema_arrange2
                if obj.up_long_ma_arrange1 is not None:
                    row.up_long_ma_arrange1 = obj.up_long_ma_arrange1
                if obj.up_long_ma_arrange2 is not None:
                    row.up_long_ma_arrange2 = obj.up_long_ma_arrange2
                if obj.up_long_ema_arrange1 is not None:
                    row.up_long_ema_arrange1 = obj.up_long_ema_arrange1
                if obj.up_long_ema_arrange2 is not None:
                    row.up_long_ema_arrange2 = obj.up_long_ema_arrange2

                if obj.down_short_ma_arrange1 is not None:
                    row.down_short_ma_arrange1 = obj.down_short_ma_arrange1
                if obj.down_short_ma_arrange2 is not None:
                    row.down_short_ma_arrange2 = obj.down_short_ma_arrange2
                if obj.down_short_ema_arrange1 is not None:
                    row.down_short_ema_arrange1 = obj.down_short_ema_arrange1
                if obj.down_short_ema_arrange2 is not None:
                    row.down_short_ema_arrange2 = obj.down_short_ema_arrange2
                if obj.down_middle_ma_arrange1 is not None:
                    row.down_middle_ma_arrange1 = obj.down_middle_ma_arrange1
                if obj.down_middle_ma_arrange2 is not None:
                    row.down_middle_ma_arrange2 = obj.down_middle_ma_arrange2
                if obj.down_middle_ema_arrange1 is not None:
                    row.down_middle_ema_arrange1 = obj.down_middle_ema_arrange1
                if obj.down_middle_ema_arrange2 is not None:
                    row.down_middle_ema_arrange2 = obj.down_middle_ema_arrange2
                if obj.down_long_ma_arrange1 is not None:
                    row.down_long_ma_arrange1 = obj.down_long_ma_arrange1
                if obj.down_long_ma_arrange2 is not None:
                    row.down_long_ma_arrange2 = obj.down_long_ma_arrange2
                if obj.down_long_ema_arrange1 is not None:
                    row.down_long_ema_arrange1 = obj.down_long_ema_arrange1
                if obj.down_long_ema_arrange2 is not None:
                    row.down_long_ema_arrange2 = obj.down_long_ema_arrange2

                if obj.ma_gold_cross1 is not None:
                    row.ma_gold_cross1 = obj.ma_gold_cross1
                if obj.ma_gold_cross2 is not None:
                    row.ma_gold_cross2 = obj.ma_gold_cross2
                if obj.ma_gold_cross3 is not None:
                    row.ma_gold_cross3 = obj.ma_gold_cross3
                if obj.ma_gold_cross4 is not None:
                    row.ma_gold_cross4 = obj.ma_gold_cross4

                if obj.ma_dead_cross1 is not None:
                    row.ma_dead_cross1 = obj.ma_dead_cross1
                if obj.ma_dead_cross2 is not None:
                    row.ma_dead_cross2 = obj.ma_dead_cross2
                if obj.ma_dead_cross3 is not None:
                    row.ma_dead_cross3 = obj.ma_dead_cross3

                if obj.ma_silver_valley is not None:
                    row.ma_silver_valley = obj.ma_silver_valley
                if obj.ma_gold_valley is not None:
                    row.ma_gold_valley = obj.ma_gold_valley

                if obj.ma_dead_valley is not None:
                    row.ma_dead_valley = obj.ma_dead_valley

                if obj.ma_out_sea is not None:
                    row.ma_out_sea = obj.ma_out_sea
                if obj.ma_hold_moon is not None:
                    row.ma_hold_moon = obj.ma_hold_moon
                if obj.ma_over_gate is not None:
                    row.ma_over_gate = obj.ma_over_gate
                if obj.ma_up_ground is not None:
                    row.ma_up_ground = obj.ma_up_ground

                if obj.ma_knife is not None:
                    row.ma_knife = obj.ma_knife
                if obj.ma_dark_cloud is not None:
                    row.ma_dark_cloud = obj.ma_dark_cloud
                if obj.ma_set_sail is not None:
                    row.ma_set_sail = obj.ma_set_sail
                if obj.ma_supreme is not None:
                    row.ma_supreme = obj.ma_supreme
                if obj.ma_dead_jump is not None:
                    row.ma_dead_jump = obj.ma_dead_jump
                if obj.ma_glue is not None:
                    row.ma_glue = obj.ma_glue

                if obj.up_ma_spider is not None:
                    row.up_ma_spider = obj.up_ma_spider
                if obj.down_ma_spider is not None:
                    row.down_ma_spider = obj.down_ma_spider

                if obj.up_hill is not None:
                    row.up_hill = obj.up_hill
                if obj.down_hill is not None:
                    row.down_hill = obj.down_hill

                if obj.up_wave is not None:
                    row.up_wave = obj.up_wave
                if obj.limit_up_gene is not None:
                    row.limit_up_gene = obj.limit_up_gene

                if obj.up_td8 is not None:
                    row.up_td8 = obj.up_td8
                if obj.up_td9 is not None:
                    row.up_td9 = obj.up_td9
                if obj.down_td8 is not None:
                    row.down_td8 = obj.down_td8
                if obj.down_td9 is not None:
                    row.down_td9 = obj.down_td9

                if obj.up_bias6 is not None:
                    row.up_bias6 = obj.up_bias6
                if obj.up_bias12 is not None:
                    row.up_bias12 = obj.up_bias12
                if obj.up_bias24 is not None:
                    row.up_bias24 = obj.up_bias24
                if obj.up_bias60 is not None:
                    row.up_bias60 = obj.up_bias60
                if obj.up_bias72 is not None:
                    row.up_bias72 = obj.up_bias72
                if obj.up_bias120 is not None:
                    row.up_bias120 = obj.up_bias120

                if obj.down_bias6 is not None:
                    row.down_bias6 = obj.down_bias6
                if obj.down_bias12 is not None:
                    row.down_bias12 = obj.down_bias12
                if obj.down_bias24 is not None:
                    row.down_bias24 = obj.down_bias24
                if obj.down_bias60 is not None:
                    row.down_bias60 = obj.down_bias60
                if obj.down_bias72 is not None:
                    row.down_bias72 = obj.down_bias72
                if obj.down_bias120 is not None:
                    row.down_bias120 = obj.down_bias120

                if obj.ma60_support is not None:
                    row.ma60_support = obj.ma60_support
                if obj.ma120_support is not None:
                    row.ma120_support = obj.ma120_support

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

                if obj.ma_down_arrange51020 is not None:
                    row.ma_down_arrange51020 = obj.ma_down_arrange51020
                if obj.ma_down_arrange5102030 is not None:
                    row.ma_down_arrange5102030 = obj.ma_down_arrange5102030
                if obj.ma_down_arrange510203060 is not None:
                    row.ma_down_arrange510203060 = obj.ma_down_arrange510203060
                if obj.ma_down_arrange203060 is not None:
                    row.ma_down_arrange203060 = obj.ma_down_arrange203060
                if obj.ma_down_arrange2060120 is not None:
                    row.ma_down_arrange2060120 = obj.ma_down_arrange2060120

                if obj.stand_up_ma60 is not None:
                    row.stand_up_ma60 = obj.stand_up_ma60
                if obj.stand_up_ma120 is not None:
                    row.stand_up_ma120 = obj.stand_up_ma120

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

                if obj.hang_neck is not None:
                    row.hang_neck = obj.hang_neck
                if obj.shooting is not None:
                    row.shooting = obj.shooting
                if obj.rise_line is not None:
                    row.rise_line = obj.rise_line
                if obj.drop_line is not None:
                    row.drop_line = obj.drop_line
                if obj.up_screw is not None:
                    row.up_screw = obj.up_screw
                if obj.down_screw is not None:
                    row.down_screw = obj.down_screw
                if obj.down_rise is not None:
                    row.down_rise = obj.down_rise

                if obj.upward_jump is not None:
                    row.upward_jump = obj.upward_jump
                if obj.downward_jump is not None:
                    row.downward_jump = obj.downward_jump
                if obj.rise_limit is not None:
                    row.rise_limit = obj.rise_limit
                if obj.drop_limit is not None:
                    row.drop_limit = obj.drop_limit
                if obj.up_cross3ma is not None:
                    row.up_cross3ma = obj.up_cross3ma
                if obj.up_cross4ma is not None:
                    row.up_cross4ma = obj.up_cross4ma
                if obj.drop_cross3ma is not None:
                    row.drop_cross3ma = obj.drop_cross3ma
                if obj.drop_cross4ma is not None:
                    row.drop_cross4ma = obj.drop_cross4ma

                if obj.ma60_first is not None:
                    row.ma60_first = obj.ma60_first
                if obj.ma60_second is not None:
                    row.ma60_second = obj.ma60_second
                if obj.ma60_third is not None:
                    row.ma60_third = obj.ma60_third
                if obj.ma60_fourth is not None:
                    row.ma60_fourth = obj.ma60_fourth
                if obj.ma60_fifth is not None:
                    row.ma60_fifth = obj.ma60_fifth
                if obj.ma60_sixth is not None:
                    row.ma60_sixth = obj.ma60_sixth
                if obj.ma60_seventh is not None:
                    row.ma60_seventh = obj.ma60_seventh
                if obj.ma60_eighth is not None:
                    row.ma60_eighth = obj.ma60_eighth

                if obj.max_vol is not None:
                    row.max_vol = obj.max_vol
                if obj.huge_vol is not None:
                    row.huge_vol = obj.huge_vol
                if obj.large_vol is not None:
                    row.large_vol = obj.large_vol
                if obj.high_vol is not None:
                    row.high_vol = obj.high_vol
                if obj.common_vol is not None:
                    row.common_vol = obj.common_vol
                if obj.low_vol is not None:
                    row.low_vol = obj.low_vol
                if obj.increase_vol is not None:
                    row.increase_vol = obj.increase_vol
                if obj.decrease_vol is not None:
                    row.decrease_vol = obj.decrease_vol
                if obj.increasingly_vol is not None:
                    row.increasingly_vol = obj.increasingly_vol
                if obj.decreasingly_vol is not None:
                    row.decreasingly_vol = obj.decreasingly_vol

                if obj.hlines is not None:
                    row.hlines = obj.hlines
                if obj.limit_pullback is not None:
                    row.limit_pullback = obj.limit_pullback
                if obj.up_pullback is not None:
                    row.up_pullback = obj.up_pullback
                if obj.down_pullback is not None:
                    row.down_pullback = obj.down_pullback
                if obj.up_break is not None:
                    row.up_break = obj.up_break
                if obj.down_break is not None:
                    row.down_break = obj.down_break
                if obj.hline_support is not None:
                    row.hline_support = obj.hline_support
                if obj.hline_resistance is not None:
                    row.hline_resistance = obj.hline_resistance

        except Exception as e:
            print('Error:', e)

        self.session.commit()
        self.session.close()
