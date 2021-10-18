# 导入:
from sqlalchemy import Column, Integer, String, Date, Float, select
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

# 创建对象的基类:
Base = declarative_base()


# 定义 candle 对象:
class DailyCandle(Base):
    # 表的名字:
    __tablename__ = 'daily_candles'

    # 表的结构:
    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    trade_date = Column(Date)  # 交易日期
    open = Column(Float)  # 开盘价
    high = Column(Float)  # 最高价
    low = Column(Float)  # 最低价
    close = Column(Float)  # 收盘价
    pre_close = Column(Float)  # 昨收价
    change = Column(Float)  # 涨跌额
    pct_chg = Column(Float)  # 涨跌幅
    vol = Column(Float)  # 成交量
    amount = Column(Float)  # 成交额
    # 每日行情指标数据
    turnover_rate = Column(Float)  # 换手率
    turnover_rate_f = Column(Float)  # 换手率(自由流通股)
    volume_ratio = Column(Float)  # 量比
    pe = Column(Float)  # 市盈率（总市值/净利润）
    pe_ttm = Column(Float)  # 市盈率（TTM）
    pb = Column(Float)  # 市净率（总市值/净资产）
    ps = Column(Float)  # 市销率
    ps_ttm = Column(Float)  # 市销率（TTM）
    dv_ratio = Column(Float)  # 股息率（%）
    dv_ttm = Column(Float)  # 股息率（TTM)（%）
    total_share = Column(Float)  # 总股本
    float_share = Column(Float)  # 流通股本
    free_share = Column(Float)  # 自由流通股本
    total_mv = Column(Float)  # 总市值
    circ_mv = Column(Float)  # 流通市值
    ma5 = Column(Float)
    ma10 = Column(Float)
    ma20 = Column(Float)
    ma30 = Column(Float)
    ma34 = Column(Float)
    ma55 = Column(Float)
    ma60 = Column(Float)
    ma120 = Column(Float)
    ma144 = Column(Float)
    ma169 = Column(Float)
    ema5 = Column(Float)
    ema10 = Column(Float)
    ema20 = Column(Float)
    ema30 = Column(Float)
    ema34 = Column(Float)
    ema55 = Column(Float)
    ema60 = Column(Float)
    ema120 = Column(Float)
    ema144 = Column(Float)
    ema169 = Column(Float)
    ma5_slope = Column(Float)
    ma10_slope = Column(Float)
    ma20_slope = Column(Float)
    ma30_slope = Column(Float)
    ma34_slope = Column(Float)
    ma55_slope = Column(Float)
    ma60_slope = Column(Float)
    ma120_slope = Column(Float)
    ma144_slope = Column(Float)
    ma169_slope = Column(Float)
    ema5_slope = Column(Float)
    ema10_slope = Column(Float)
    ema20_slope = Column(Float)
    ema30_slope = Column(Float)
    ema34_slope = Column(Float)
    ema55_slope = Column(Float)
    ema60_slope = Column(Float)
    ema120_slope = Column(Float)
    ema144_slope = Column(Float)
    ema169_slope = Column(Float)
    diff = Column(Float)
    dea = Column(Float)
    macd = Column(Float)
    bias6 = Column(Float)
    bias12 = Column(Float)
    bias24 = Column(Float)
    bias60 = Column(Float)


def get_obj(candle):
    candle = candle.to_dict()
    candle = {k: v if not pd.isna(v) else None for k, v in candle.items()}

    return DailyCandle(
        ts_code=candle.get('ts_code', None),
        trade_date=candle.get('trade_date', None),
        open=candle.get('open', None),
        high=candle.get('high', None),
        low=candle.get('low', None),
        close=candle.get('close', None),
        pre_close=candle.get('pre_close', None),
        change=candle.get('change', None),
        pct_chg=candle.get('pct_chg', None),
        vol=candle.get('vol', None),
        amount=candle.get('amount', None),
        # 每日行情指标数据
        turnover_rate=candle.get('turnover_rate', None),
        turnover_rate_f=candle.get('turnover_rate_f', None),
        volume_ratio=candle.get('volume_ratio', None),
        pe=candle.get('pe', None),
        pe_ttm=candle.get('pe_ttm', None),
        pb=candle.get('pb', None),
        ps=candle.get('ps', None),
        ps_ttm=candle.get('ps_ttm', None),
        dv_ratio=candle.get('dv_ratio', None),
        dv_ttm=candle.get('dv_ttm', None),
        total_share=candle.get('total_share', None),
        float_share=candle.get('float_share', None),
        free_share=candle.get('free_share', None),
        total_mv=candle.get('total_mv', None),
        circ_mv=candle.get('circ_mv', None),
        # 技术指标
        ma5=candle.get('ma5', None),
        ma10=candle.get('ma10', None),
        ma20=candle.get('ma20', None),
        ma30=candle.get('ma30', None),
        ma34=candle.get('ma34', None),
        ma55=candle.get('ma55', None),
        ma60=candle.get('ma60', None),
        ma120=candle.get('ma120', None),
        ma144=candle.get('ma144', None),
        ma169=candle.get('ma169', None),
        ema5=candle.get('ema5', None),
        ema10=candle.get('ema10', None),
        ema20=candle.get('ema20', None),
        ema30=candle.get('ema30', None),
        ema34=candle.get('ema34', None),
        ema55=candle.get('ema55', None),
        ema60=candle.get('ema60', None),
        ema120=candle.get('ema120', None),
        ema144=candle.get('ema144', None),
        ema169=candle.get('ema169', None),
        ma5_slope=candle.get('ma5_slope', None),
        ma10_slope=candle.get('ma10_slope', None),
        ma20_slope=candle.get('ma20_slope', None),
        ma30_slope=candle.get('ma30_slope', None),
        ma34_slope=candle.get('ma34_slope', None),
        ma55_slope=candle.get('ma55_slope', None),
        ma60_slope=candle.get('ma60_slope', None),
        ma120_slope=candle.get('ma120_slope', None),
        ma144_slope=candle.get('ma144_slope', None),
        ma169_slope=candle.get('ma169_slope', None),
        ema5_slope=candle.get('ema5_slope', None),
        ema10_slope=candle.get('ema10_slope', None),
        ema20_slope=candle.get('ema20_slope', None),
        ema30_slope=candle.get('ema30_slope', None),
        ema34_slope=candle.get('ema34_slope', None),
        ema55_slope=candle.get('ema55_slope', None),
        ema60_slope=candle.get('ema60_slope', None),
        ema120_slope=candle.get('ema120_slope', None),
        ema144_slope=candle.get('ema144_slope', None),
        ema169_slope=candle.get('ema169_slope', None),
        diff=candle.get('diff', None),
        dea=candle.get('dea', None),
        macd=candle.get('macd', None),
        bias6=candle.get('bias6', None),
        bias12=candle.get('bias12', None),
        bias24=candle.get('bias24', None),
        bias60=candle.get('bias60', None),
    )


class DailyCandleDao:
    def __init__(self):
        self.session = DBSession()

    def find_all(self, ts_code):
        statement = select(DailyCandle).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().all()

        return result

    def add_one(self, candle):
        obj = get_obj(candle)

        rows = self.session.query(DailyCandle.id).filter(DailyCandle.ts_code == candle['ts_code']).filter(
            DailyCandle.trade_date == candle['trade_date']).first()

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

            self.session.bulk_insert_mappings(DailyCandle, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def bulk_upsert(self, df):

        for index, candle in df.iterrows():
            obj = get_obj(candle)

            try:
                row = self.session.query(DailyCandle).filter(DailyCandle.ts_code == candle['ts_code']).filter(
                    DailyCandle.trade_date == candle['trade_date']).first()

                if row is None:
                    self.session.add(obj)
                else:
                    if obj.open is not None:
                        row.open = obj.open
                    if obj.high is not None:
                        row.high = obj.high
                    if obj.low is not None:
                        row.low = obj.low
                    if obj.close is not None:
                        row.close = obj.close
                    if obj.pre_close is not None:
                        row.pre_close = obj.pre_close
                    if obj.change is not None:
                        row.change = obj.change
                    if obj.pct_chg is not None:
                        row.pct_chg = obj.pct_chg
                    if obj.vol is not None:
                        row.vol = obj.vol
                    if obj.amount is not None:
                        row.amount = obj.amount
                    if obj.turnover_rate is not None:
                        row.turnover_rate = obj.turnover_rate
                    if obj.turnover_rate_f is not None:
                        row.turnover_rate_f = obj.turnover_rate_f
                    if obj.volume_ratio is not None:
                        row.volume_ratio = obj.volume_ratio
                    if obj.pe is not None:
                        row.pe = obj.pe
                    if obj.pe_ttm is not None:
                        row.pe_ttm = obj.pe_ttm
                    if obj.pb is not None:
                        row.pb = obj.pb
                    if obj.ps is not None:
                        row.ps = obj.ps
                    if obj.ps_ttm is not None:
                        row.ps_ttm = obj.ps_ttm
                    if obj.dv_ratio is not None:
                        row.dv_ratio = obj.dv_ratio
                    if obj.dv_ttm is not None:
                        row.dv_ttm = obj.dv_ttm
                    if obj.total_share is not None:
                        row.total_share = obj.total_share
                    if obj.float_share is not None:
                        row.float_share = obj.float_share
                    if obj.free_share is not None:
                        row.free_share = obj.free_share
                    if obj.total_mv is not None:
                        row.total_mv = obj.total_mv
                    if obj.circ_mv is not None:
                        row.circ_mv = obj.circ_mv
                    if obj.ma5 is not None:
                        row.ma5 = obj.ma5
                    if obj.ma10 is not None:
                        row.ma10 = obj.ma10
                    if obj.ma20 is not None:
                        row.ma20 = obj.ma20
                    if obj.ma30 is not None:
                        row.ma30 = obj.ma30
                    if obj.ma34 is not None:
                        row.ma34 = obj.ma34
                    if obj.ma55 is not None:
                        row.ma55 = obj.ma55
                    if obj.ma60 is not None:
                        row.ma60 = obj.ma60
                    if obj.ma120 is not None:
                        row.ma120 = obj.ma120
                    if obj.ma144 is not None:
                        row.ma144 = obj.ma44
                    if obj.ma169 is not None:
                        row.ma169 = obj.ma169
                    if obj.ema5 is not None:
                        row.ema5 = obj.ema5
                    if obj.ema10 is not None:
                        row.ema10 = obj.ema10
                    if obj.ema20 is not None:
                        row.ema20 = obj.ema20
                    if obj.ema30 is not None:
                        row.ema30 = obj.ema30
                    if obj.ema34 is not None:
                        row.ema34 = obj.ema34
                    if obj.ema55 is not None:
                        row.ema55 = obj.ema55
                    if obj.ema60 is not None:
                        row.ema60 = obj.ema60
                    if obj.ema120 is not None:
                        row.ema120 = obj.ema120
                    if obj.ema144 is not None:
                        row.ema144 = obj.ema144
                    if obj.ema169 is not None:
                        row.ema169 = obj.ema169
                    if obj.diff is not None:
                        row.diff = obj.diff
                    if obj.dea is not None:
                        row.dea = obj.dea
                    if obj.macd is not None:
                        row.macd = obj.macd
                    if obj.bias6 is not None:
                        row.bias6 = obj.bias6
                    if obj.bias12 is not None:
                        row.bias12 = obj.bias12
                    if obj.bias24 is not None:
                        row.bias24 = obj.bias24
                    if obj.bias60 is not None:
                        row.bias60 = obj.bias60

            except Exception as e:
                print('Error:', e)

            self.session.commit()
        self.session.close()

        return df
