from sqlalchemy import Column, Integer, String, Date, SmallInteger, select
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class StockShortSignal(Base):
    __tablename__ = 'stock_short_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    # 技术信号
    ma30_down = Column(SmallInteger)
    ema30_down = Column(SmallInteger)
    ma60_down = Column(SmallInteger)
    ema60_down = Column(SmallInteger)
    ma120_down = Column(SmallInteger)
    ema120_down = Column(SmallInteger)
    ma_arrange = Column(SmallInteger)
    ema_arrange = Column(SmallInteger)
    short_ma_arrange_1 = Column(SmallInteger)
    short_ma_arrange_2 = Column(SmallInteger)
    short_ema_arrange_1 = Column(SmallInteger)
    short_ema_arrange_2 = Column(SmallInteger)
    middle_ma_arrange_1 = Column(SmallInteger)
    middle_ma_arrange_2 = Column(SmallInteger)
    middle_ema_arrange_1 = Column(SmallInteger)
    middle_ema_arrange_2 = Column(SmallInteger)
    long_ma_arrange_1 = Column(SmallInteger)
    long_ma_arrange_2 = Column(SmallInteger)
    long_ema_arrange_1 = Column(SmallInteger)
    long_ema_arrange_2 = Column(SmallInteger)
    ma_dead_cross_1 = Column(SmallInteger)
    ma_dead_cross_2 = Column(SmallInteger)
    ma_dead_cross_3 = Column(SmallInteger)
    ema_dead_cross_1 = Column(SmallInteger)
    ema_dead_cross_2 = Column(SmallInteger)
    ema_dead_cross_3 = Column(SmallInteger)
    ma_dead_valley = Column(SmallInteger)
    ema_dead_valley = Column(SmallInteger)
    ma_knife = Column(SmallInteger)
    ema_knife = Column(SmallInteger)
    ma_dark_cloud = Column(SmallInteger)
    ema_dark_cloud = Column(SmallInteger)
    ma_set_sail = Column(SmallInteger)
    ema_set_sail = Column(SmallInteger)
    ma_supreme = Column(SmallInteger)
    ema_supreme = Column(SmallInteger)
    ma_dead_jump = Column(SmallInteger)
    ema_dead_jump = Column(SmallInteger)
    ma_spider = Column(SmallInteger)
    ma_spider_2 = Column(SmallInteger)
    ema_spider = Column(SmallInteger)
    ema_spider_2 = Column(SmallInteger)
    td_8 = Column(SmallInteger)
    td_9 = Column(SmallInteger)


def get_obj(signal):
    signal = signal.to_dict()
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return StockShortSignal(
        ts_code=signal.get('ts_code', None),
        # 技术信号
        ma30_down=signal.get('ma30_down', None),
        ema30_down=signal.get('ema30_down', None),
        ma60_down=signal.get('ma60_down', None),
        ema60_down=signal.get('ema60_down', None),
        ma120_down=signal.get('ma120_down', None),
        ema120_down=signal.get('ema120_down', None),
        ma_arrange=signal.get('ma_arrange', None),
        ema_arrange=signal.get('ema_arrange', None),
        short_ma_arrange_1=signal.get('short_ma_arrange_1', None),
        short_ma_arrange_2=signal.get('short_ma_arrange_2', None),
        short_ema_arrange_1=signal.get('short_ema_arrange_1', None),
        short_ema_arrange_2=signal.get('short_ema_arrange_2', None),
        middle_ma_arrange_1=signal.get('middle_ma_arrange_1', None),
        middle_ma_arrange_2=signal.get('middle_ma_arrange_2', None),
        middle_ema_arrange_1=signal.get('middle_ema_arrange_1', None),
        middle_ema_arrange_2=signal.get('middle_ema_arrange_2', None),
        long_ma_arrange_1=signal.get('long_ma_arrange_1', None),
        long_ma_arrange_2=signal.get('long_ma_arrange_2', None),
        long_ema_arrange_1=signal.get('long_ema_arrange_1', None),
        long_ema_arrange_2=signal.get('long_ema_arrange_2', None),
        ma_dead_cross_1=signal.get('ma_dead_cross_1', None),
        ma_dead_cross_2=signal.get('ma_dead_cross_2', None),
        ma_dead_cross_3=signal.get('ma_dead_cross_3', None),
        ema_dead_cross_1=signal.get('ema_dead_cross_1', None),
        ema_dead_cross_2=signal.get('ema_dead_cross_2', None),
        ema_dead_cross_3=signal.get('ema_dead_cross_3', None),
        ma_dead_valley=signal.get('ma_dead_valley', None),
        ema_dead_valley=signal.get('ema_dead_valley', None),
        ma_knife=signal.get('ma_knife', None),
        ema_knife=signal.get('ema_knife', None),
        ma_dark_cloud=signal.get('ma_dark_cloud', None),
        ema_dark_cloud=signal.get('ema_dark_cloud', None),
        ma_set_sail=signal.get('ma_set_sail', None),
        ema_set_sail=signal.get('ema_set_sail', None),
        ma_supreme=signal.get('ma_supreme', None),
        ema_supreme=signal.get('ema_supreme', None),
        ma_dead_jump=signal.get('ma_dead_jump', None),
        ema_dead_jump=signal.get('ema_dead_jump', None),
        ma_spider=signal.get('ma_spider', None),
        ma_spider_2=signal.get('ma_spider_2', None),
        ema_spider=signal.get('ema_spider', None),
        ema_spider_2=signal.get('ema_spider_2', None),
        td_8=signal.get('td_8', None),
        td_9=signal.get('td_9', None)
    )


class StockShortSignalDao:
    def __init__(self):
        self.session = DBSession()

    def upsert(self, signal):

        obj = get_obj(signal)

        try:
            row = self.session.query(StockShortSignal).filter(StockShortSignal.ts_code == signal['ts_code']).first()

            if row is None:
                self.session.add(obj)
            else:
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
                if obj.ma_arrange is not None:
                    row.ma_arrange = obj.ma_arrange
                if obj.ema_arrange is not None:
                    row.ema_arrange = obj.ema_arrange
                if obj.short_ma_arrange_1 is not None:
                    row.short_ma_arrange_1 = obj.short_ma_arrange_1
                if obj.short_ma_arrange_2 is not None:
                    row.short_ma_arrange_2 = obj.short_ma_arrange_2
                if obj.short_ema_arrange_1 is not None:
                    row.short_ema_arrange_1 = obj.short_ema_arrange_1
                if obj.short_ema_arrange_2 is not None:
                    row.short_ema_arrange_2 = obj.short_ema_arrange_2
                if obj.middle_ma_arrange_1 is not None:
                    row.middle_ma_arrange_1 = obj.middle_ma_arrange_1
                if obj.middle_ma_arrange_2 is not None:
                    row.middle_ma_arrange_2 = obj.middle_ma_arrange_2
                if obj.middle_ema_arrange_1 is not None:
                    row.middle_ema_arrange_1 = obj.middle_ema_arrange_1
                if obj.middle_ema_arrange_2 is not None:
                    row.middle_ema_arrange_2 = obj.middle_ema_arrange_2
                if obj.long_ma_arrange_1 is not None:
                    row.long_ma_arrange_1 = obj.long_ma_arrange_1
                if obj.long_ma_arrange_2 is not None:
                    row.long_ma_arrange_2 = obj.long_ma_arrange_2
                if obj.long_ema_arrange_1 is not None:
                    row.long_ema_arrange_1 = obj.long_ema_arrange_1
                if obj.long_ema_arrange_2 is not None:
                    row.long_ema_arrange_2 = obj.long_ema_arrange_2
                if obj.ma_dead_cross_1 is not None:
                    row.ma_dead_cross_1 = obj.ma_dead_cross_1
                if obj.ma_dead_cross_2 is not None:
                    row.ma_dead_cross_2 = obj.ma_dead_cross_2
                if obj.ma_dead_cross_3 is not None:
                    row.ma_dead_cross_3 = obj.ma_dead_cross_3
                if obj.ema_dead_cross_1 is not None:
                    row.ema_dead_cross_1 = obj.ema_dead_cross_1
                if obj.ema_dead_cross_2 is not None:
                    row.ema_dead_cross_2 = obj.ema_dead_cross_2
                if obj.ema_dead_cross_3 is not None:
                    row.ema_dead_cross_3 = obj.ema_dead_cross_3
                if obj.ma_dead_valley is not None:
                    row.ma_dead_valley = obj.ma_dead_valley
                if obj.ema_dead_valley is not None:
                    row.ema_dead_valley = obj.ema_dead_valley
                if obj.ma_knife is not None:
                    row.ma_knife = obj.ma_knife
                if obj.ema_knife is not None:
                    row.ema_knife = obj.ema_knife
                if obj.ma_dark_cloud is not None:
                    row.ma_dark_cloud = obj.ma_dark_cloud
                if obj.ema_dark_cloud is not None:
                    row.ema_dark_cloud = obj.ema_dark_cloud
                if obj.ma_set_sail is not None:
                    row.ma_set_sail = obj.ma_set_sail
                if obj.ema_set_sail is not None:
                    row.ema_set_sail = obj.ema_set_sail
                if obj.ma_supreme is not None:
                    row.ma_supreme = obj.ma_supreme
                if obj.ema_supreme is not None:
                    row.ema_supreme = obj.ema_supreme
                if obj.ma_dead_jump is not None:
                    row.ma_dead_jump = obj.ma_dead_jump
                if obj.ema_dead_jump is not None:
                    row.ema_dead_jump = obj.ema_dead_jump
                if obj.ma_spider is not None:
                    row.ma_spider = obj.ma_spider
                if obj.ma_spider_2 is not None:
                    row.ma_spider_2 = obj.ma_spider_2
                if obj.ema_spider is not None:
                    row.ema_spider = obj.ema_spider
                if obj.ema_spider_2 is not None:
                    row.ema_spider_2 = obj.ema_spider_2
                if obj.td_8 is not None:
                    row.td_8 = obj.td_8
                if obj.td_9 is not None:
                    row.td_9 = obj.td_9

        except Exception as e:
            print('Error:', e)

        self.session.commit()
        self.session.close()
