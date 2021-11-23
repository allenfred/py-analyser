from sqlalchemy import Column, Integer, String, Date, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class StockAnalyticSignal(Base):
    __tablename__ = 'stock_analytic_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)
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
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return StockAnalyticSignal(
        ts_code=signal.get('ts_code', None),
        exchange=signal.get('exchange', None),
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


class StockAnalyticSignalDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_ts_code(self, ts_code):
        s = text("select * from stock_analytic_signals where ts_code = :ts_code "
                 "order by trade_date desc limit 0,500;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['ts_code'])
        self.session.close()

        return df

    def find_all(self, ts_code):
        statement = select(StockAnalyticSignal).filter_by(ts_code=ts_code)
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

            self.session.bulk_insert_mappings(StockAnalyticSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def reinsert(self, df, ts_code):
        self.session.execute("delete from stock_analytic_signals where ts_code = :ts_code", {"ts_code": ts_code})
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(StockAnalyticSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()

    def upsert(self, signal):
        obj = get_obj(signal)

        try:
            row = self.session.query(StockAnalyticSignal). \
                filter(StockAnalyticSignal.ts_code == signal['ts_code']).first()

            if row is None:
                self.session.add(obj)
            else:
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

        except Exception as e:
            print('Error:', e)

        self.session.commit()
        self.session.close()
