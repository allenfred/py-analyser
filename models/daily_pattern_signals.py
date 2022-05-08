from sqlalchemy import Column, Integer, String, Date, SmallInteger, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

Base = declarative_base()


class DailyPatternSignal(Base):
    __tablename__ = 'daily_pattern_signals'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)
    trade_date = Column(Date)  # 交易日期
    exchange = Column(String)  # 交易所代码

    # 一日K线形态
    CDLCLOSINGMARUBOZU = Column(SmallInteger)
    CDLDOJI = Column(SmallInteger)
    CDLDOJISTAR = Column(SmallInteger)
    CDLDRAGONFLYDOJI = Column(SmallInteger)
    CDLGRAVESTONEDOJI = Column(SmallInteger)
    CDLHAMMER = Column(SmallInteger)
    CDLHANGINGMAN = Column(SmallInteger)
    CDLLONGLEGGEDDOJI = Column(SmallInteger)
    CDLLONGLINE = Column(SmallInteger)
    CDLMARUBOZU = Column(SmallInteger)
    CDLRICKSHAWMAN = Column(SmallInteger)
    CDLSHOOTINGSTAR = Column(SmallInteger)
    CDLSHORTLINE = Column(SmallInteger)
    CDLTAKURI = Column(SmallInteger)

    # 两日K线形态
    CDLCOUNTERATTACK = Column(SmallInteger)
    CDLDARKCLOUDCOVER = Column(SmallInteger)
    CDLGAPSIDESIDEWHITE = Column(SmallInteger)
    CDLHARAMI = Column(SmallInteger)
    CDLHARAMICROSS = Column(SmallInteger)
    CDLHOMINGPIGEON = Column(SmallInteger)
    CDLINNECK = Column(SmallInteger)
    CDLKICKING = Column(SmallInteger)
    CDLKICKINGBYLENGTH = Column(SmallInteger)
    CDLMATCHINGLOW = Column(SmallInteger)
    CDLDRAGONFLYDOJI = Column(SmallInteger)
    CDLONNECK = Column(SmallInteger)
    CDLSEPARATINGLINES = Column(SmallInteger)
    CDLTHRUSTING = Column(SmallInteger)
    CDLBELTHOLD = Column(SmallInteger)
    CDLENGULFING = Column(SmallInteger)
    CDLPIERCING = Column(SmallInteger)

    # 三日K线形态
    CDL2CROWS = Column(SmallInteger)
    CDL3BLACKCROWS = Column(SmallInteger)
    CDL3INSIDE = Column(SmallInteger)
    CDL3OUTSIDE = Column(SmallInteger)
    CDL3STARSINSOUTH = Column(SmallInteger)
    CDLABANDONEDBABY = Column(SmallInteger)
    CDLUNIQUE3RIVER = Column(SmallInteger)
    CDLMORNINGSTAR = Column(SmallInteger)
    CDLMORNINGDOJISTAR = Column(SmallInteger)
    CDLEVENINGSTAR = Column(SmallInteger)
    CDLEVENINGDOJISTAR = Column(SmallInteger)
    CDL3WHITESOLDIERS = Column(SmallInteger)
    CDLADVANCEBLOCK = Column(SmallInteger)
    CDLHIGHWAVE = Column(SmallInteger)
    CDLHIKKAKE = Column(SmallInteger)
    CDLHIKKAKEMOD = Column(SmallInteger)
    CDLIDENTICAL3CROWS = Column(SmallInteger)
    CDLSPINNINGTOP = Column(SmallInteger)
    CDLSTALLEDPATTERN = Column(SmallInteger)
    CDLSTICKSANDWICH = Column(SmallInteger)
    CDLTASUKIGAP = Column(SmallInteger)
    CDLTRISTAR = Column(SmallInteger)
    CDLUPSIDEGAP2CROWS = Column(SmallInteger)
    CDL3LINESTRIKE = Column(SmallInteger)

    # 四日K线形态
    CDLCONCEALBABYSWALL = Column(SmallInteger)
    CDLBREAKAWAY = Column(SmallInteger)

    # 五日K线形态
    CDLLADDERBOTTOM = Column(SmallInteger)
    CDLMATHOLD = Column(SmallInteger)
    CDLRISEFALL3METHODS = Column(SmallInteger)
    CDLXSIDEGAP3METHODS = Column(SmallInteger)


def get_obj(signal):
    signal = {k: v if not pd.isna(v) else None for k, v in signal.items()}

    return StockDailySignal(
        ts_code=signal.get('ts_code', None),
        trade_date=signal.get('trade_date', None),
        exchange=signal.get('exchange', None),
        CDLCLOSINGMARUBOZU=signal.get('CDLCLOSINGMARUBOZU', None),
        CDLDOJI=signal.get('CDLDOJI', None),
        CDLDOJISTAR=signal.get('CDLDOJISTAR', None),
        CDLDRAGONFLYDOJI=signal.get('CDLDRAGONFLYDOJI', None),
        CDLGRAVESTONEDOJI=signal.get('CDLGRAVESTONEDOJI', None),
        CDLHAMMER=signal.get('CDLHAMMER', None),
        CDLHANGINGMAN=signal.get('CDLHANGINGMAN', None),
        CDLLONGLEGGEDDOJI=signal.get('CDLLONGLEGGEDDOJI', None),
        CDLLONGLINE=signal.get('CDLLONGLINE', None),
        CDLMARUBOZU=signal.get('CDLMARUBOZU', None),
        CDLRICKSHAWMAN=signal.get('CDLRICKSHAWMAN', None),
        CDLSHOOTINGSTAR=signal.get('CDLSHOOTINGSTAR', None),
        CDLSHORTLINE=signal.get('CDLSHORTLINE', None),
        CDLTAKURI=signal.get('CDLTAKURI', None),
        CDLCOUNTERATTACK=signal.get('CDLCOUNTERATTACK', None),
        CDLDARKCLOUDCOVER=signal.get('CDLDARKCLOUDCOVER', None),
        CDLGAPSIDESIDEWHITE=signal.get('CDLGAPSIDESIDEWHITE', None),
        CDLHARAMI=signal.get('CDLHARAMI', None),
        CDLHARAMICROSS=signal.get('CDLHARAMICROSS', None),
        CDLHOMINGPIGEON=signal.get('CDLHOMINGPIGEON', None),
        CDLINNECK=signal.get('CDLINNECK', None),
        CDLKICKING=signal.get('CDLKICKING', None),
        CDLKICKINGBYLENGTH=signal.get('CDLKICKINGBYLENGTH', None),
        CDLMATCHINGLOW=signal.get('CDLMATCHINGLOW', None),
        CDLONNECK=signal.get('CDLONNECK', None),
        CDLSEPARATINGLINES=signal.get('CDLSEPARATINGLINES', None),
        CDLTHRUSTING=signal.get('CDLTHRUSTING', None),
        CDLBELTHOLD=signal.get('CDLBELTHOLD', None),
        CDLENGULFING=signal.get('CDLENGULFING', None),
        CDLPIERCING=signal.get('CDLPIERCING', None),
        CDL2CROWS=signal.get('CDL2CROWS', None),
        CDL3BLACKCROWS=signal.get('CDL3BLACKCROWS', None),
        CDL3INSIDE=signal.get('CDL3INSIDE', None),
        CDL3OUTSIDE=signal.get('CDL3OUTSIDE', None),
        CDL3STARSINSOUTH=signal.get('CDL3STARSINSOUTH', None),
        CDLABANDONEDBABY=signal.get('CDLABANDONEDBABY', None),
        CDLUNIQUE3RIVER=signal.get('CDLUNIQUE3RIVER', None),
        CDLMORNINGSTAR=signal.get('CDLMORNINGSTAR', None),
        CDLMORNINGDOJISTAR=signal.get('CDLMORNINGDOJISTAR', None),
        CDLEVENINGSTAR=signal.get('CDLEVENINGSTAR', None),
        CDLEVENINGDOJISTAR=signal.get('CDLEVENINGDOJISTAR', None),
        CDL3WHITESOLDIERS=signal.get('CDL3WHITESOLDIERS', None),
        CDLADVANCEBLOCK=signal.get('CDLADVANCEBLOCK', None),
        CDLHIGHWAVE=signal.get('CDLHIGHWAVE', None),
        CDLHIKKAKE=signal.get('CDLHIKKAKE', None),
        CDLHIKKAKEMOD=signal.get('CDLHIKKAKEMOD', None),
        CDLIDENTICAL3CROWS=signal.get('CDLIDENTICAL3CROWS', None),
        CDLSPINNINGTOP=signal.get('CDLSPINNINGTOP', None),
        CDLSTALLEDPATTERN=signal.get('CDLSTALLEDPATTERN', None),
        CDLSTICKSANDWICH=signal.get('CDLSTICKSANDWICH', None),
        CDLTASUKIGAP=signal.get('CDLTASUKIGAP', None),
        CDLTRISTAR=signal.get('CDLTRISTAR', None),
        CDLUPSIDEGAP2CROWS=signal.get('CDLUPSIDEGAP2CROWS', None),
        CDL3LINESTRIKE=signal.get('CDL3LINESTRIKE', None),
        CDLCONCEALBABYSWALL=signal.get('CDLCONCEALBABYSWALL', None),
        CDLBREAKAWAY=signal.get('CDLBREAKAWAY', None),
        CDLLADDERBOTTOM=signal.get('CDLLADDERBOTTOM', None),
        CDLMATHOLD=signal.get('CDLMATHOLD', None),
        CDLRISEFALL3METHODS=signal.get('CDLRISEFALL3METHODS', None),
        CDLXSIDEGAP3METHODS=signal.get('CDLXSIDEGAP3METHODS', None),
    )


class DailyPatternSignalDao:
    def __init__(self):
        self.session = DBSession()

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date from daily_pattern_signals where ts_code = :ts_code "
                 "order by trade_date desc limit 0,20;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date'])
        self.session.close()

        return df

    def find_all(self, ts_code):
        statement = select(DailyPatternSignal).filter_by(ts_code=ts_code)
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
            self.session.bulk_insert_mappings(DailyPatternSignal, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()