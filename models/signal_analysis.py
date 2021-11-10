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
    weak_bias60_support = Column(SmallInteger)
    strong_bias60_support = Column(SmallInteger)
    weak_bias120_support = Column(SmallInteger)
    strong_bias120_support = Column(SmallInteger)


def get_obj(signal):
    signal = signal.to_dict()
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return SignalAnalysis(
        ts_code=signal.get('ts_code', None),
        trade_date=signal.get('trade_date', None),
        exchange=item.get('exchange', None),
        weak_bias60_support=signal.get('weak_bias60_support', None),
        strong_bias60_support=signal.get('strong_bias60_support', None),
        weak_bias120_support=signal.get('weak_bias120_support', None),
        strong_bias120_support=signal.get('strong_bias120_support', None),
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
                    if obj.weak_bias60_support is not None:
                        row.weak_bias60_support = obj.weak_bias60_support
                    if obj.strong_bias60_support is not None:
                        row.strong_bias60_support = obj.strong_bias60_support
                    if obj.weak_bias120_support is not None:
                        row.weak_bias120_support = obj.weak_bias120_support
                    if obj.strong_bias120_support is not None:
                        row.strong_bias120_support = obj.strong_bias120_support

            except Exception as e:
                print('Error:', e)

            self.session.commit()
        self.session.close()

        return df

    def reinsert(self, df):
        ts_code = df['ts_code'][0]
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
