from sqlalchemy import Column, Integer, String, Date, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class SignalAnalysis(Base):
    __tablename__ = 'signal_analysis'

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
    yearly_price_position1020 = Column(SmallInteger)
    yearly_price_position2030 = Column(SmallInteger)
    yearly_price_position3050 = Column(SmallInteger)
    yearly_price_position5070 = Column(SmallInteger)
    yearly_price_position70100 = Column(SmallInteger)

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


def get_obj(signal):
    signal = signal.to_dict()
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return SignalAnalysis(
        ts_code=signal.get('ts_code', None),
        trade_date=signal.get('trade_date', None),
        exchange=item.get('exchange', None),
        ma60_support=signal.get('ma60_support', None),
        ema60_support=signal.get('ema60_support', None),
        ma120_support=signal.get('ma120_support', None),
        ema120_support=signal.get('ema120_support', None),

        yearly_price_position=signal.get('yearly_price_position', None),
        yearly_price_position10=signal.get('yearly_price_position10', None),
        yearly_price_position1020=signal.get('yearly_price_position1020', None),
        yearly_price_position2030=signal.get('yearly_price_position2030', None),
        yearly_price_position3050=signal.get('yearly_price_position3050', None),
        yearly_price_position5070=signal.get('yearly_price_position5070', None),
        yearly_price_position70100=signal.get('yearly_price_position70100', None),

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
    )


class SignalAnalysisDao:
    def __init__(self):
        self.session = DBSession()

    def find_all(self, ts_code):
        statement = select(SignalAnalysis).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().all()

        return result

    def add_one(self, signal):
        obj = get_obj(signal)

        rows = self.session.query(SignalAnalysis.id).filter(SignalAnalysis.ts_code == signal['ts_code']).filter(
            SignalAnalysis.trade_date == signal['trade_date']).first()

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

            self.session.bulk_insert_mappings(SignalAnalysis, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def bulk_upsert(self, df):
        for index, signal in df.iterrows():
            obj = get_obj(signal)
            try:
                row = self.session.query(SignalAnalysis).filter(SignalAnalysis.ts_code == signal['ts_code']).filter(
                    SignalAnalysis.trade_date == signal['trade_date']).first()

                if row is None:
                    self.session.add(obj)
                else:
                    if obj.ma60_support is not None:
                        row.ma60_support = obj.ma60_support
                    if obj.ma120_support is not None:
                        row.ma120_support = obj.ma120_support
                    if obj.ema60_support is not None:
                        row.ema60_support = obj.ema60_support
                    if obj.ema120_support is not None:
                        row.ema120_support = obj.ema120_support

            except Exception as e:
                print('Error:', e)

            self.session.commit()
        self.session.close()

        return df

    def reinsert(self, df, ts_code):
        self.session.execute("delete from signal_analysis where ts_code = :ts_code", {"ts_code": ts_code})
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(SignalAnalysis, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()
