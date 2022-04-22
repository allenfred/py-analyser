from sqlalchemy import Column, Integer, String, Date, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class DailyShortSignal(Base):
    __tablename__ = 'daily_short_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)
    trade_date = Column(Date)  # 交易日期
    ma20_down = Column(SmallInteger)
    ema20_down = Column(SmallInteger)
    ma30_down = Column(SmallInteger)
    ema30_down = Column(SmallInteger)
    ma60_down = Column(SmallInteger)
    ema60_down = Column(SmallInteger)
    ma120_down = Column(SmallInteger)
    ema120_down = Column(SmallInteger)
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
    ma_dead_cross1 = Column(SmallInteger)
    ma_dead_cross2 = Column(SmallInteger)
    ma_dead_cross3 = Column(SmallInteger)
    ema_dead_cross1 = Column(SmallInteger)
    ema_dead_cross2 = Column(SmallInteger)
    ema_dead_cross3 = Column(SmallInteger)
    ma_dead_valley = Column(SmallInteger)
    ema_dead_valley = Column(SmallInteger)
    ma_knife = Column(SmallInteger)   # MA 断头铡刀(5/10/20)
    ema_knife = Column(SmallInteger)   # EMA 断头铡刀(5/10/20)
    ma_dark_cloud = Column(SmallInteger)  # MA 乌云密布
    ema_dark_cloud = Column(SmallInteger)  # EMA 乌云密布
    ma_set_sail = Column(SmallInteger)  # MA 战机起航
    ema_set_sail = Column(SmallInteger)  # EMA 战机起航
    ma_supreme = Column(SmallInteger)  # MA 气贯长虹(5/10/20)
    ema_supreme = Column(SmallInteger)  # EMA 气贯长虹(5/10/20)
    ma_dead_jump = Column(SmallInteger)  # MA绝命跳(5/10/20)
    ema_dead_jump = Column(SmallInteger)  # EMA绝命跳(5/10/20)
    ma_spider = Column(SmallInteger)  # MA毒蜘蛛(5/10/20)
    ma_spider2 = Column(SmallInteger)  # MA毒蜘蛛(5/10/20/30)
    ema_spider = Column(SmallInteger)  # EMA毒蜘蛛(5/10/20)
    ema_spider2 = Column(SmallInteger)   # EMA毒蜘蛛(5/10/20/30)
    td8 = Column(SmallInteger)
    td9 = Column(SmallInteger)
    bias6 = Column(SmallInteger)
    bias12 = Column(SmallInteger)
    bias24 = Column(SmallInteger)
    bias60 = Column(SmallInteger)
    bias72 = Column(SmallInteger)
    bias120 = Column(SmallInteger)


def get_obj(signal):
    signal = signal.to_dict()
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return DailyShortSignal(
        ts_code=signal.get('ts_code', None),
        trade_date=signal.get('trade_date', None),
        ma20_down=signal.get('ma20_down', None),
        ema20_down=signal.get('ema20_down', None),
        ma30_down=signal.get('ma30_down', None),
        ema30_down=signal.get('ema30_down', None),
        ma60_down=signal.get('ma60_down', None),
        ema60_down=signal.get('ema60_down', None),
        ma120_down=signal.get('ma120_down', None),
        ema120_down=signal.get('ema120_down', None),
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
        ma_dead_cross1=signal.get('ma_dead_cross1', None),
        ma_dead_cross2=signal.get('ma_dead_cross2', None),
        ma_dead_cross3=signal.get('ma_dead_cross3', None),
        ema_dead_cross1=signal.get('ema_dead_cross1', None),
        ema_dead_cross2=signal.get('ema_dead_cross2', None),
        ema_dead_cross3=signal.get('ema_dead_cross3', None),
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
    )


class DailyShortSignalDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date from daily_short_signals where ts_code = :ts_code "
                 "order by trade_date desc limit 0,500;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date'])
        self.session.close()

        return df

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

    def bulk_insert(self, df, ts_code):
        db_df = self.find_by_ts_code(ts_code)
        insert_needed_df = df.loc[~df["trade_date"].isin(db_df["trade_date"].to_numpy())]

        items = []
        for index, item in insert_needed_df.iterrows():
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