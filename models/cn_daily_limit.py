from sqlalchemy import Column, Integer, String, Date, DateTime, Float, select, text, update, bindparam
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import literal_column
from .db import engine, DBSession
import pandas as pd
from datetime import datetime, date
import mysql.connector

Base = declarative_base()


class CNDailyCandle(Base):
    __tablename__ = 'cn_daily_candles'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ts_code = Column(String)  # TS代码
    name = Column(String)  # 股票名称
    trade_date = Column(Date)  # 交易日期
    close = Column(Float)  # 收盘价
    pct_chg = Column(Float)  # 涨跌幅
    amp = Column(Float)  # 振幅
    vol = Column(Float)  # 成交量
    fc_ratio = Column(Float)  # 封单金额/日成交金额
    fl_ratio = Column(Float)  # 封单手数/流通股本
    fd_amount = Column(Float)  # 封单金额
    first_time = Column(DateTime)  # 首次涨停时间
    last_time = Column(DateTime)  # 最后封板时间
    open_times = Column(Integer)  # 打开次数
    strth = Column(Float)  # 涨跌停强度
    limit = Column(String)  # D跌停U涨停


def get_obj(candle):
    candle = candle.to_dict()
    candle = {k: v if not pd.isna(v) else None for k, v in candle.items()}

    return CNDailyCandle(
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


class CNDailyCandleDao:
    def __init__(self):
        self.session = DBSession()

    def find_latest_candle(self):
        s = text("select trade_date, open, close, high, low from cn_daily_candles order by trade_date desc limit 1;")
        statement = self.session.execute(s.params())
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'close', 'high', 'low'])
        self.session.close()

        if len(df):
            return df.iloc[0]
        else:
            return None

    def find_by_ts_code(self, ts_code):
        s = text("select trade_date, open, close, high, low from cn_daily_candles where ts_code = :ts_code "
                 "order by trade_date desc limit 0,2000;")
        statement = self.session.execute(s.params(ts_code=ts_code))
        df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'close', 'high', 'low'])
        self.session.close()

        return df

    def find_by_trade_date(self, trade_date):
        s = text("select ts_code, open, close, high, low from cn_daily_candles where trade_date = :trade_date;")
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
            self.session.bulk_insert_mappings(CNDailyCandle, items)
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
            self.session.execute("delete from cn_daily_candles where ts_code = :ts_code "
                                 "order by trade_date desc limit :limit",
                                 {"ts_code": ts_code, "limit": len(df)})
            self.session.bulk_insert_mappings(CNDailyCandle, items)
            self.session.commit()
        except Exception as e:
            print('Error:', e)

        self.session.close()
        return len(df)

    def bulk_upsert(self, df):

        for index, candle in df.iterrows():
            obj = get_obj(candle)

            try:
                row = self.session.query(CNDailyCandle).filter(CNDailyCandle.ts_code == candle['ts_code']).filter(
                    CNDailyCandle.trade_date == candle['trade_date']).first()

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

    def bulk_update(self, df):
        if len(df) == 0:
            return 0

        conn = mysql.connector.connect(host="8.210.170.98", user='dev',
                                       password='dev123456', database='quant')
        cursor = conn.cursor()
        ts_code = df['ts_code'][0]
        querysql = 'select id, trade_date, open, high, low, close from cn_daily_candles ' \
                   'where ts_code = %s order by trade_date desc  limit 0,%s;'
        cursor.execute(querysql, (ts_code, len(df)))
        db_df = pd.DataFrame(cursor.fetchall(), columns=['id', 'trade_date', 'open', 'high', 'low', 'close'])

        updated_rows_cnt = 0
        for item in db_df.itertuples():
            dte = datetime.strftime(item.trade_date, "%Y%m%d")
            i = df[df['trade_date'] == dte].iloc[0]

            if not (i.open == item.open and i.high == item.high and i.low == item.low and i.close == item.close):
                updated_rows_cnt += 1
                sql = 'update cn_daily_candles set open = %s, high = %s, low = %s, close = %s ' \
                      'where id = %s;'
                cursor.execute(sql, (float(i.open), float(i.high), float(i.low), float(i.close), item.id))

        conn.commit()
        cursor.close()

        return updated_rows_cnt
