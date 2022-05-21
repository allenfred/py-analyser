from sqlalchemy import Column, Integer, String, Date, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class WeeklySignal(Base):
    __tablename__ = 'weekly_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    trade_date = Column(Date)  # 交易日期

    ma20_up = Column(SmallInteger)
    ema20_up = Column(SmallInteger)
    ma30_up = Column(SmallInteger)
    ema30_up = Column(SmallInteger)
    ma60_up = Column(SmallInteger)
    ema60_up = Column(SmallInteger)
    ma20_down = Column(SmallInteger)
    ema20_down = Column(SmallInteger)
    ma30_down = Column(SmallInteger)
    ema30_down = Column(SmallInteger)
    ma60_down = Column(SmallInteger)
    ema60_down = Column(SmallInteger)

    up_ma_arrange = Column(SmallInteger)
    up_ema_arrange = Column(SmallInteger)
    down_ma_arrange = Column(SmallInteger)
    down_ema_arrange = Column(SmallInteger)

    up_short_ma_arrange1 = Column(SmallInteger)
    up_short_ma_arrange2 = Column(SmallInteger)
    up_short_ema_arrange1 = Column(SmallInteger)
    up_short_ema_arrange2 = Column(SmallInteger)

    down_short_ma_arrange1 = Column(SmallInteger)
    down_short_ma_arrange2 = Column(SmallInteger)

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
    ma_group_glue = Column(SmallInteger)

    up_hill = Column(SmallInteger)
    down_hill = Column(SmallInteger)

    ma60_support = Column(SmallInteger)

    ma_up_arrange51020 = Column(SmallInteger)
    ma_up_arrange5102030 = Column(SmallInteger)
    ma_up_arrange510203060 = Column(SmallInteger)
    ma_down_arrange51020 = Column(SmallInteger)
    ma_down_arrange5102030 = Column(SmallInteger)
    ma_down_arrange510203060 = Column(SmallInteger)

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
    up_screw = Column(SmallInteger)
    down_screw = Column(SmallInteger)


def get_obj(signal):
    signal = signal.to_dict()
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return WeeklySignal(
        ts_code=signal.get('ts_code', None),
        trade_date=signal.get('trade_date', None),
        # 技术信号
        ma20_up=signal.get('ma20_up', None),
        ema20_up=signal.get('ema20_up', None),
        ma30_up=signal.get('ma30_up', None),
        ema30_up=signal.get('ema30_up', None),
        ma60_up=signal.get('ma60_up', None),
        ema60_up=signal.get('ema60_up', None),
        ma20_down=signal.get('ma20_down', None),
        ema20_down=signal.get('ema20_down', None),
        ma30_down=signal.get('ma30_down', None),
        ema30_down=signal.get('ema30_down', None),
        ma60_down=signal.get('ma60_down', None),
        ema60_down=signal.get('ema60_down', None),

        up_ma_arrange=signal.get('up_ma_arrange', None),
        up_ema_arrange=signal.get('up_ema_arrange', None),
        down_ma_arrange=signal.get('down_ma_arrange', None),
        down_ema_arrange=signal.get('down_ema_arrange', None),

        up_short_ma_arrange1=signal.get('up_short_ma_arrange1', None),
        up_short_ma_arrange2=signal.get('up_short_ma_arrange2', None),
        up_short_ema_arrange1=signal.get('up_short_ema_arrange1', None),
        up_short_ema_arrange2=signal.get('up_short_ema_arrange2', None),
        down_short_ma_arrange1=signal.get('down_short_ma_arrange1', None),
        down_short_ma_arrange2=signal.get('down_short_ma_arrange2', None),

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
        ma_group_glue=signal.get('ma_group_glue', None),

        up_hill=signal.get('up_hill', None),
        down_hill=signal.get('down_hill', None),

        ma60_support=signal.get('ma60_support', None),

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
        up_screw=signal.get('up_screw', None),
        down_screw=signal.get('down_screw', None),
    )


class WeeklySignalDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date from weekly_signals where ts_code = :ts_code "
                 "order by trade_date desc limit 0,500;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date'])
        self.session.close()

        return df

    def find_all(self, ts_code):
        statement = select(WeeklySignal).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().all()

        return result

    def add_one(self, signal):
        obj = get_obj(signal)

        rows = self.session.query(WeeklySignal.id).filter(WeeklySignal.ts_code == signal['ts_code']).filter(
            WeeklySignal.trade_date == signal['trade_date']).first()

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
            self.session.bulk_insert_mappings(WeeklySignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def reinsert(self, df, ts_code):
        self.session.execute("delete from weekly_signals where ts_code = :ts_code", {"ts_code": ts_code})
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(WeeklySignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()
