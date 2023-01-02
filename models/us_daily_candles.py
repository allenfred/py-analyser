import pymysql.cursors
from sqlalchemy import Column, Integer, String, Date, Float, select, text
from sqlalchemy.ext.declarative import declarative_base
from .db import DBSession
import pandas as pd

# 创建对象的基类:
Base = declarative_base()


# 定义 candle 对象:
class USDailyCandle(Base):
    # 表的名字:
    __tablename__ = 'us_daily_candles'

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


def get_obj(candle):
    candle = candle.to_dict()
    candle = {k: v if not pd.isna(v) else None for k, v in candle.items()}

    return USDailyCandle(
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
        circ_mv=candle.get('circ_mv', None)
    )


class USDailyCandleDao:
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

    def find_latest_candle(self):
        s = text("select trade_date, open, close, high, low from us_daily_candles order by trade_date desc limit 1;")
        statement = self.session.execute(s.params())
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'close', 'high', 'low'])
        self.session.close()

        if len(df):
            return df.iloc[0]
        else:
            return None

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date, open, close, high, low from us_daily_candles where ts_code = :ts_code "
                 "order by trade_date desc limit 0,2000;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'close', 'high', 'low'])
        self.session.close()

        return df

    def find_by_trade_date(self, trade_date):
        s = text("select ts_code, open, close, high, low from us_daily_candles where trade_date = :trade_date;")
        statement = self.session.execute(s.params(trade_date=trade_date))
        df = pd.DataFrame(statement.fetchall(), columns=['ts_code', 'open', 'close', 'high', 'low'])
        self.session.close()

        return df

    def bulk_insert(self, df):
        items = []
        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}

            if item['ts_code'] is not None and item['trade_date'] is not None:
                items.insert(index, item)

        try:
            self.session.bulk_insert_mappings(USDailyCandle, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            self.session.close()

    def reinsert(self, df):
        ts_code = df['ts_code'][0]
        items = []

        for index, item in df.iterrows():
            item = item.to_dict()
            item = {k: v if not pd.isna(v) else None for k, v in item.items()}
            items.insert(index, item)

        try:
            self.session.execute("delete from us_daily_candles where ts_code = :ts_code", {"ts_code": ts_code})
            self.session.bulk_insert_mappings(USDailyCandle, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()

    def bulk_upsert(self, df):

        for index, candle in df.iterrows():
            obj = get_obj(candle)

            try:
                row = self.session.query(USDailyCandle).filter(USDailyCandle.ts_code == candle['ts_code']).filter(
                    USDailyCandle.trade_date == candle['trade_date']).first()

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

            except Exception as e:
                print('Error:', e)

            self.session.commit()
        self.session.close()

        return df

    def load_local_file(self, path):
        self.open_connection()

        with self.conn:
            with self.conn.cursor() as cursor:
                # ts_code, trade_date, close, open, high, low, chg, pre_close, pct_chg, vol, amount, total_mv, pe, pb, turnover_rate

                # Create a new record
                sql = """
                LOAD DATA LOCAL INFILE %s INTO TABLE us_daily_candles
                FIELDS TERMINATED BY ","
                LINES TERMINATED BY "\n"
                IGNORE 1 LINES 
                (ts_code, trade_date, @close, @open, @high, @low, @chg, @pre_close, @pct_chg, @vol, @amount, @total_mv, @pe, @pb, @turnover_rate)
                SET
                close = NULLIF(@close,0),
                open = NULLIF(@open,0),
                high = NULLIF(@high,0),
                low = NULLIF(@low,0),
                chg = NULLIF(@chg,0),
                pre_close = NULLIF(@pre_close,0),
                pct_chg = NULLIF(@pct_chg,0),
                vol = NULLIF(@vol,0),
                amount = NULLIF(@amount,0),
                total_mv = NULLIF(@total_mv,0),
                pe = NULLIF(@pe,0),
                pb = NULLIF(@pb,0),
                turnover_rate = NULLIF(@turnover_rate,0);
                """
                # sql = """
                #                 LOAD DATA LOCAL INFILE %s INTO TABLE us_daily_candles
                #                 FIELDS TERMINATED BY ","
                #                 LINES TERMINATED BY "\n"
                #                 IGNORE 1 LINES
                #                 (@vone, @vtwo, @vthree, @vfour, @vfive)
                #                 SET
                #                 one = NULLIF(@vone,''),
                #                 two = NULLIF(@vtwo,''),
                #                 three = NULLIF(@vthree,''),
                #                 four = NULLIF(@vfour,'');
                #                 """
                cursor.execute(sql, (path))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()
