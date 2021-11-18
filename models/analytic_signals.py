from sqlalchemy import Column, Integer, String, Date, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class AnalyticSignal(Base):
    __tablename__ = 'analytic_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)
    trade_date = Column(Date)
    exchange = Column(String)  # 交易所 CN HK US
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


def get_obj(signal):
    signal = signal.to_dict()
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return AnalyticSignal(
        ts_code=signal.get('ts_code', None),
        trade_date=signal.get('trade_date', None),
        exchange=item.get('exchange', None),
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
    )


class AnalyticSignalDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date from analytic_signals where ts_code = :ts_code "
                 "order by trade_date desc limit 0,500;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date'])
        self.session.close()

        return df

    def find_all(self, ts_code):
        statement = select(AnalyticSignal).filter_by(ts_code=ts_code)
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

            self.session.bulk_insert_mappings(AnalyticSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def reinsert(self, df, ts_code, session):
        # self.session.execute("delete from analytic_signals where ts_code = :ts_code", {"ts_code": ts_code})
        session.execute("delete from analytic_signals where ts_code = :ts_code", {"ts_code": ts_code})
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            session.bulk_insert_mappings(AnalyticSignal, items)
            session.commit()
        except Exception as e:
            print('Error:', e)

        session.close()
