# 导入:
from sqlalchemy import Column, Integer, String, Date, SmallInteger, Float, select
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

# 创建对象的基类:
Base = declarative_base()


def get_obj(stock):
    stock = stock.to_dict()
    stock = {k: v if not pd.isna(v) else None for k, v in stock.items()}

    return Stock(
        ts_code=stock.get('ts_code', None),
        symbol=stock.get('symbol', None),
        name=stock.get('name', None),
        area=stock.get('area', None),
        industry=stock.get('industry', None),
        fullname=stock.get('fullname', None),
        enname=stock.get('enname', None),
        cnspell=stock.get('cnspell', None),
        market=stock.get('market', None),
        exchange=stock.get('exchange', None),
        list_status=stock.get('list_status', None),
        list_date=stock.get('list_date', None),
        delist_date=stock.get('delist_date', None),
        is_hs=stock.get('is_hs', None),
        turnover_rate=stock.get('turnover_rate', None),
        turnover_rate_f=stock.get('turnover_rate_f', None),
        volume_ratio=stock.get('volume_ratio', None),
        pe=stock.get('pe', None),
        pe_ttm=stock.get('pe_ttm', None),
        pb=stock.get('pb', None),
        ps=stock.get('ps', None),
        ps_ttm=stock.get('ps_ttm', None),
        dv_ratio=stock.get('dv_ratio', None),
        dv_ttm=stock.get('dv_ttm', None),
        total_share=stock.get('total_share', None),
        float_share=stock.get('float_share', None),
        free_share=stock.get('free_share', None),
        total_mv=stock.get('total_mv', None),
        circ_mv=stock.get('circ_mv', None),
    )

# 定义 Stock 对象:
class Stock(Base):
    # 表的名字:
    __tablename__ = 'stocks'

    # 表的结构:
    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String, unique=True)  # TS代码
    symbol = Column(String, unique=True)  # 股票代码
    name = Column(String)  # 股票名称
    area = Column(String)  # 地域
    industry = Column(String)  # 所属行业
    fullname = Column(String)  # 股票全称
    enname = Column(String)  # 英文全称
    cnspell = Column(String)  # 拼音缩写
    market = Column(String)  # 市场类型
    exchange = Column(String)  # 交易所代码
    list_status = Column(String)  # 上市状态 L上市 D退市 P暂停上市
    list_date = Column(Date)  # 上市日期
    delist_date = Column(Date)  # 退市日期
    is_hs = Column(String)  # 是否沪深港通标的，N否 H沪股通 S深股通
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


class StockDao:
    def __init__(self):
        self.session = DBSession()

    def find_one(self, ts_code):
        statement = select(Stock).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().first()

        return result

    def add_one(self, stock):
        obj = get_obj(stock)

        rows = self.session.query(Stock.id).filter(Stock.ts_code == stock['ts_code']).all()

        if len(rows) == 0:
            self.session.add(obj)

        self.session.commit()
        self.session.close()

        return obj

    def batch_add(self, df):

        for index, stock in df.iterrows():
            obj = get_obj(stock)

            row = self.session.query(Stock).filter(Stock.ts_code == stock.get('ts_code')).first()

            if row is None:
                self.session.add(obj)
            else:
                if obj.symbol is not None:
                    row.symbol = obj.symbol
                if obj.name is not None:
                    row.name = obj.name
                if obj.area is not None:
                    row.name = obj.area
                if obj.industry is not None:
                    row.industry = obj.industry
                if obj.fullname is not None:
                    row.fullname = obj.fullname
                if obj.enname is not None:
                    row.enname = obj.enname
                if obj.cnspell is not None:
                    row.cnspell = obj.cnspell
                if obj.market is not None:
                    row.market = obj.market
                if obj.exchange is not None:
                    row.exchange = obj.exchange
                if obj.list_status is not None:
                    row.list_status = obj.list_status
                if obj.list_date is not None:
                    row.list_date = obj.list_date
                if obj.delist_date is not None:
                    row.delist_date = obj.delist_date
                if obj.is_hs is not None:
                    row.is_hs = obj.is_hs
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

            self.session.commit()

        self.session.close()

        return df
