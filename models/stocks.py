import pymysql.cursors

from sqlalchemy import Table, MetaData, Column, Integer, String, Date, SmallInteger, Float, select, insert, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql.dml import Insert
from .db import engine, DBSession
import pandas as pd
from datetime import datetime, date

Base = declarative_base()
conn = engine.connect()
metadata_obj = MetaData()


class Stock(Base):
    __tablename__ = 'stocks'

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
    scan_date = Column(Date)  # 上一次扫描完成日期
    candle_date = Column(Date)  # 上一次获取candle完成日期
    indicator_date = Column(Date)  # 上一次计算indicator完成日期
    weekly_date = Column(Date)  # 上一次计算weekly candle完成日期
    amount = Column(Float)  # 最近一个交易日的成交额
    ex_date = Column(Date)  # 除权除息日
    close = Column(Float)  # 最新价


stocks = Table('stocks', metadata_obj,
               Column('id', Integer, primary_key=True),
               Column('ts_code', String),
               Column('symbol', String),
               Column('name', String),
               Column('area', String),
               Column('industry', String),
               Column('fullname', String),
               Column('enname', String),
               Column('cnspell', String),
               Column('market', String),
               Column('exchange', String),
               Column('list_status', String),
               Column('list_date', Date),
               Column('delist_date', Date),
               Column('is_hs', String),
               Column('turnover_rate', Float),
               Column('turnover_rate_f', Float),
               Column('volume_ratio', Float),
               Column('pe', Float),
               Column('pe_ttm', Float),
               Column('pb', Float),
               Column('ps', Float),
               Column('ps_ttm', Float),
               Column('dv_ratio', Float),
               Column('dv_ttm', Float),
               Column('total_share', Float),
               Column('float_share', Float),
               Column('free_share', Float),
               Column('total_mv', Float),
               Column('circ_mv', Float),
               Column('scan_date', Date),
               Column('candle_date', Date),
               Column('indicator_date', Date),
               Column('weekly_date', Date),
               Column('amount', Float),
               Column('ex_date', Date),
               Column('close', Float),
               )


def get_obj(item):
    item = item.to_dict()
    item = {k: v if not pd.isna(v) else None for k, v in item.items()}

    return Stock(
        ts_code=item.get('ts_code', None),
        symbol=item.get('symbol', None),
        name=item.get('name', None),
        area=item.get('area', None),
        industry=item.get('industry', None),
        fullname=item.get('fullname', None),
        enname=item.get('enname', None),
        cnspell=item.get('cnspell', None),
        market=item.get('market', None),
        exchange=item.get('exchange', None),
        list_status=item.get('list_status', None),
        list_date=item.get('list_date', None),
        delist_date=item.get('delist_date', None),
        is_hs=item.get('is_hs', None),
        turnover_rate=item.get('turnover_rate', None),
        turnover_rate_f=item.get('turnover_rate_f', None),
        volume_ratio=item.get('volume_ratio', None),
        pe=item.get('pe', None),
        pe_ttm=item.get('pe_ttm', None),
        pb=item.get('pb', None),
        ps=item.get('ps', None),
        ps_ttm=item.get('ps_ttm', None),
        dv_ratio=item.get('dv_ratio', None),
        dv_ttm=item.get('dv_ttm', None),
        total_share=item.get('total_share', None),
        float_share=item.get('float_share', None),
        free_share=item.get('free_share', None),
        total_mv=item.get('total_mv', None),
        circ_mv=item.get('circ_mv', None),
        scan_date=item.get('scan_date', None),
        candle_date=item.get('candle_date', None),
        indicator_date=item.get('indicator_date', None),
        weekly_date=item.get('weekly_date', None),
        amount=item.get('amount', None),  # 成交额
        ex_date=item.get('ex_date', None),  # 除权除息日
        close=item.get('close', None),  # 最新价
    )


class StockDao:
    def __init__(self):
        self.session = DBSession()

    def open_connection(self):
        # Connect to the database
        self.conn = pymysql.connect(host='121.4.15.211',
                                    user='dev',
                                    password='04f5d5a3b91006a8',
                                    database='quant',
                                    local_infile=1,
                                    cursorclass=pymysql.cursors.DictCursor)

    def find_all(self, exchange):
        exchange_query = " exchange = 'SSE' or exchange = 'SZSE' "
        if exchange == 'HK':
            exchange_query = "exchange = 'HK'"
        if exchange == 'US':
            exchange_query = "exchange = 'US'"

        stock_stmts = self.session.execute(text("select "
                                                "id, ts_code, symbol, name, area, industry, "
                                                "fullname, enname, cnspell, market, exchange, list_status, "
                                                "list_date, delist_date, is_hs, turnover_rate, turnover_rate_f, "
                                                "volume_ratio, pe, pe_ttm, pb, ps, ps_ttm, dv_ratio, dv_ttm, "
                                                "total_share, float_share, free_share, total_mv, circ_mv, "
                                                "scan_date, candle_date, indicator_date, weekly_date, amount, "
                                                "ex_date, close "
                                                "from stocks where " + exchange_query))

        stocks = pd.DataFrame(stock_stmts.fetchall(), columns=["id", "ts_code", "symbol", "name", "area", "industry",
                                                               "fullname", "enname", "cnspell", "market", "exchange",
                                                               "list_status",
                                                               "list_date", "delist_date", "is_hs", "turnover_rate",
                                                               "turnover_rate_f",
                                                               "volume_ratio", "pe", "pe_ttm", "pb", "ps", "ps_ttm",
                                                               "dv_ratio", "dv_ttm",
                                                               "total_share", "float_share", "free_share", "total_mv",
                                                               "circ_mv",
                                                               "scan_date", "candle_date", "indicator_date",
                                                               "weekly_date", "amount",
                                                               "ex_date", "close"])

        self.session.close()

        return stocks

    def find_one_candle_not_ready(self, area, candle_date):
        exchange_query = "(exchange = 'SSE' or exchange = 'SZSE')"
        if area == 'HK':
            exchange_query = "exchange = 'HK'"
        if area == 'US':
            exchange_query = "exchange = 'US'"

        stock_stmts = self.session.execute(text("select ts_code from stocks where (candle_date is null or candle_date"
                                                " < :candle_date) and "
                                                + exchange_query + "  limit 1").params(
            candle_date=candle_date))
        stock_result = stock_stmts.fetchone()
        self.session.close()

        if len(stock_result) > 0:
            return stock_result[0]
        else:
            return None

    def find_one_weekly_not_ready(self, cur_date):
        stock_stmts = self.session.execute(text("select ts_code from stocks where (weekly_date is null or weekly_date"
                                                " < :cur_date) and "
                                                "(exchange = 'SSE' or exchange = 'SZSE')  limit 1").params(
            cur_date=cur_date))
        stock_result = stock_stmts.fetchone()
        self.session.close()

        if stock_result and len(stock_result) > 0:
            return stock_result[0]
        else:
            return None

    def find_one_indicator_not_ready(self, area, indicator_date):
        exchange_query = "(exchange = 'SSE' or exchange = 'SZSE')"
        if area == 'HK':
            exchange_query = "exchange = 'HK'"
        if area == 'US':
            exchange_query = "exchange = 'US'"

        stock_stmts = self.session.execute(text("select ts_code from stocks where (indicator_date is null "
                                                "or indicator_date < :indicator_date) and "
                                                + exchange_query + "  limit 1").params(
            indicator_date=indicator_date))
        stock_result = stock_stmts.fetchone()
        self.session.close()

        if len(stock_result) > 0:
            return stock_result[0]
        else:
            return None

    def find_one(self, ts_code):
        statement = select(Stock).filter_by(ts_code=ts_code)
        result = self.session.execute(statement).scalars().first()
        self.session.close()

        return result

    def add_one(self, item):
        obj = get_obj(item)

        rows = self.session.query(Stock.id).filter(Stock.ts_code == item['ts_code']).all()

        if len(rows) == 0:
            self.session.add(obj)

        self.session.commit()
        self.session.close()

        return obj

    def update(self, obj):
        obj = {k: v if not pd.isna(v) else None for k, v in obj.items()}

        try:
            row = self.session.query(Stock).filter(Stock.ts_code == obj.get('ts_code')).first()

            if row:
                if obj.get('symbol') is not None:
                    row.symbol = obj.get('symbol')
                if obj.get('name') is not None:
                    row.name = obj.get('name')
                if obj.get('area') is not None:
                    row.name = obj.get('area')
                if obj.get('industry') is not None:
                    row.industry = obj.get('industry')
                if obj.get('fullname') is not None:
                    row.fullname = obj.get('fullname')
                if obj.get('enname') is not None:
                    row.enname = obj.get('enname')
                if obj.get('cnspell') is not None:
                    row.cnspell = obj.get('cnspell')
                if obj.get('market') is not None:
                    row.market = obj.get('market')
                if obj.get('exchange') is not None:
                    row.exchange = obj.get('exchange')
                if obj.get('list_status') is not None:
                    row.list_status = obj.get('list_status')
                if obj.get('list_date') is not None:
                    row.list_date = obj.get('list_date')
                if obj.get('delist_date') is not None:
                    row.delist_date = obj.get('delist_date')
                if obj.get('is_hs') is not None:
                    row.is_hs = obj.get('is_hs')
                if obj.get('turnover_rate') is not None:
                    row.turnover_rate = obj.get('turnover_rate')
                if obj.get('turnover_rate_f') is not None:
                    row.turnover_rate_f = obj.get('turnover_rate_f')
                if obj.get('volume_ratio') is not None:
                    row.volume_ratio = obj.get('volume_ratio')
                if obj.get('pe') is not None:
                    row.pe = obj.get('pe')
                if obj.get('pe_ttm') is not None:
                    row.pe_ttm = obj.get('pe_ttm')
                if obj.get('pb') is not None:
                    row.pb = obj.get('pb')
                if obj.get('ps') is not None:
                    row.ps = obj.get('ps')
                if obj.get('ps_ttm') is not None:
                    row.ps_ttm = obj.get('ps_ttm')
                if obj.get('dv_ratio') is not None:
                    row.dv_ratio = obj.get('dv_ratio')
                if obj.get('dv_ttm') is not None:
                    row.dv_ttm = obj.get('dv_ttm')
                if obj.get('total_share') is not None:
                    row.total_share = obj.get('total_share')
                if obj.get('float_share') is not None:
                    row.float_share = obj.get('float_share')
                if obj.get('free_share') is not None:
                    row.free_share = obj.get('free_share')
                if obj.get('total_mv') is not None:
                    row.total_mv = obj.get('total_mv')
                if obj.get('circ_mv') is not None:
                    row.circ_mv = obj.get('circ_mv')
                if obj.get('scan_date') is not None:
                    row.scan_date = obj.get('scan_date')
                if obj.get('candle_date') is not None:
                    row.candle_date = obj.get('candle_date')
                if obj.get('indicator_date') is not None:
                    row.indicator_date = obj.get('indicator_date')
                if obj.get('weekly_date') is not None:
                    row.weekly_date = obj.get('weekly_date')
                if obj.get('amount') is not None:
                    row.amount = obj.get('amount')
                if obj.get('ex_date') is not None:
                    row.ex_date = obj.get('ex_date')
                if obj.get('close') is not None:
                    row.close = obj.get('close')

        except Exception as e:
            print('Error:', e)

        self.session.commit()
        self.session.close()

    def bulk_insert(self, df):
        items = []
        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            if item.get('exchange') != 'BSE':
                items.insert(index, item)

        self.session.bulk_insert_mappings(Stock, items)
        self.session.commit()
        self.session.close()

    def bulk_upsert(self, df):
        for index, item in df.iterrows():
            obj = get_obj(item)
            try:
                row = self.session.query(Stock).filter(Stock.ts_code == obj.ts_code).first()

                if row is None:
                    self.session.add(obj)
                else:
                    if obj.symbol is not None:
                        row.symbol = obj.symbol
                    if obj.name is not None:
                        row.name = obj.name
                    if obj.area is not None:
                        row.area = obj.area
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
                    if obj.amount is not None:
                        row.amount = obj.amount
                    if obj.ex_date is not None:
                        row.ex_date = obj.ex_date
                    if obj.close is not None:
                        row.close = obj.close

            except Exception as e:
                print('Error:', e)

        self.session.commit()

        self.session.close()

        return df

    def update_us_from_file(self, path):
        self.open_connection()

        with self.conn:
            with self.conn.cursor() as cursor:
                # replace all to update

                sql = """
                      LOAD DATA LOCAL INFILE %s REPLACE INTO TABLE stocks
                      FIELDS TERMINATED BY ","
                      LINES TERMINATED BY "\n"
                      IGNORE 1 LINES 
                      (id, ts_code, symbol, name, area, industry, 
                        fullname, enname, cnspell, market, exchange, list_status, 
                        list_date, delist_date, is_hs, 
                        @turnover_rate, @turnover_rate_f, @volume_ratio, @pe, 
                        @pe_ttm, @pb, @ps, @ps_ttm, @dv_ratio, @dv_ttm, 
                        @total_share, @float_share, @free_share, @total_mv, @circ_mv, 
                        @scan_date, @candle_date, @indicator_date, @weekly_date, @amount, 
                        @ex_date, @close)
                      SET
                        turnover_rate = NULLIF(@turnover_rate,0),
                        turnover_rate_f = NULLIF(@turnover_rate_f,0),
                        volume_ratio = NULLIF(@volume_ratio,0),
                        pe = NULLIF(@pe,0),
                        pe_ttm = NULLIF(@pe_ttm,0),
                        pb = NULLIF(@pb,0),
                        ps = NULLIF(@ps,0),
                        ps_ttm = NULLIF(@ps_ttm,0),
                        dv_ratio = NULLIF(@dv_ratio,0),
                        dv_ttm = NULLIF(@dv_ttm,0),
                        total_share = NULLIF(@total_share,0),
                        float_share = NULLIF(@float_share,0),
                        free_share = NULLIF(@free_share,0),
                        total_mv = NULLIF(@total_mv,0),
                        circ_mv = NULLIF(@circ_mv,0),
                        scan_date = NULLIF(@scan_date,""),
                        candle_date = NULLIF(@candle_date,""),
                        indicator_date = NULLIF(@indicator_date,""),
                        weekly_date = NULLIF(@weekly_date,""),
                        ex_date = NULLIF(@ex_date,""),
                        amount = NULLIF(@amount,0),
                        close = NULLIF(@close,0);
                      """

                cursor.execute(sql, path)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()
