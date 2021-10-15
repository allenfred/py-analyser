# 导入:
from sqlalchemy import Column, Integer, String, Date, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class CNStock(Base):
    # 表的名字:
    __tablename__ = 'cn_stocks'

    # 表的结构:
    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String,unique=True)  # TS代码
    symbol = Column(String,unique=True)  # 股票代码
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


class CNStockDao:
    def __init__(self):
        self.session = DBSession()

    def add_one(self, stock):
        obj = CNStock(
            ts_code=stock['ts_code'],
            symbol=stock['symbol'],
            name=stock['name'],
            area=stock['area'],
            industry=stock['industry'],
            fullname=stock['fullname'],
            enname=stock['enname'],
            cnspell=stock['cnspell'],
            market=stock['market'],
            exchange=stock['exchange'],
            list_status=stock['list_status'],
            list_date=stock['list_date'],
            delist_date=stock['delist_date'],
            is_hs=stock['is_hs'],
        )

        rows = self.session.query(CNStock.id).filter(CNStock.ts_code == stock['ts_code']).all()

        if len(rows) == 0:
            self.session.add(obj)

        self.session.commit()
        self.session.close()

        return obj

    def batch_add(self, df):

        for index, stock in df.iterrows():
            obj = CNStock(
                ts_code=stock['ts_code'],
                symbol=stock['symbol'],
                name=stock['name'],
                area=stock['area'],
                industry=stock['industry'],
                fullname=stock['fullname'],
                enname=stock['enname'],
                cnspell=stock['cnspell'],
                market=stock['market'],
                exchange=stock['exchange'],
                list_status=stock['list_status'],
                list_date=stock['list_date'],
                delist_date=stock['delist_date'],
                is_hs=stock['is_hs'],
            )

            rows = self.session.query(CNStock.id).filter(CNStock.ts_code == stock['ts_code']).all()

            if len(rows) == 0:
                self.session.add(obj)

            self.session.commit()

        self.session.close()

        return df
