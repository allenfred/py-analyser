import pandas as pd
import numpy as np
import mplfinance as mpf
import matplotlib.dates as mpl_dates
from sqlalchemy import text

from models.cn_daily_candles import CNDailyCandleDao
from mongo.df import get_klines_df

dailyCandleDao = CNDailyCandleDao()


def get_stock_klines(ts_code, cnt=300):
    statement = dailyCandleDao.session.execute(
        text("select trade_date, open, high, close, low, pct_chg, amount*1000 as volume "
             "from "
             + "cn_daily_candles" + " where ts_code = :ts_code "
             + "and trade_date > '2020-01-01' and open is not null "
               "and close is not null and high is not null and"
             + " low is not null "
             + "order by trade_date desc "
               "limit :cnt").params(ts_code=ts_code, cnt=cnt))

    kline_df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'high', 'close',
                                                           'low', 'pct_chg', 'volume'])

    df = kline_df
    df = df.sort_values(by='trade_date', ascending=True)
    df['date'] = pd.to_datetime(df.trade_date)
    df = df.set_index('date')
    df['date'] = df['trade_date'].apply(mpl_dates.date2num)

    df = df.loc[:, ['date', 'open', 'high', 'low', 'close', 'volume']]

    return df


def get_crypto_klines(exchange, inst_id, gran, cnt=300):
    return get_klines_df(exchange, inst_id, gran, cnt)
