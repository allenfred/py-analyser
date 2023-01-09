import pandas as pd
import numpy as np
import mplfinance as mpf
import matplotlib.dates as mpl_dates
from sqlalchemy import text
from klines import get_stock_klines, get_crypto_klines
import lib.signal.common.hline_fractal as Hlines

from models.cn_daily_candles import CNDailyCandleDao

dailyCandleDao = CNDailyCandleDao()

# # 002918.SZ 蒙娜丽莎
# ts_code = "002918.SZ"
# ts_code = "600062.SH"
ts_code = "603027.SH"
ts_code = "002728.SZ"
ts_code = "002317.SZ"
ts_code = "002168.SZ"
ts_code = "002007.SZ"
ts_code = "000815.SZ"
# ts_code = "002432.SZ"
# ts_code = "300482.SZ"
# ts_code = "600010.SH"
ts_code = "000610.SZ"  # 西安旅游
ts_code = "000721.SZ"  # 西安饮食
ts_code = "002264.SZ"  # 北化股份
ts_code = "002246.SZ"  # 北化股份
ts_code = '002246.SZ'  # 湖南发展
ts_code = '000716.SZ'  # 黑芝麻

ts_code = '000722.SZ'  # 湖南发展
ts_code = '002799.SZ'  # 湖南发展
ts_code = '002246.SZ'  # 湖南发展
ts_code = '000721.SZ'  # 西安饮食
ts_code = '600056.SH'  # 中国医药
# ts_code = '000610.SZ'  # 西安旅游
ts_code = '000721.SZ'  # 西安饮食

statement = dailyCandleDao.session.execute(
    text("select trade_date, open, high, close, low, pct_chg, amount*1000 as volume "
         "from "
         + "cn_daily_candles" + " where ts_code = :ts_code "
         + "and trade_date > '2020-01-01' and open is not null "
         # " and trade_date < '2022-10-27' "
           "and close is not null and high is not null and"
         + " low is not null "
         + "order by trade_date desc "
           "limit 300").params(ts_code=ts_code))

kline_df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'high', 'close',
                                                       'low', 'pct_chg', 'volume'])

df = kline_df
df = df.sort_values(by='trade_date', ascending=True)
df['date'] = pd.to_datetime(df.trade_date)
df = df.set_index('date')
df['date'] = df['trade_date'].apply(mpl_dates.date2num)

df = df.loc[:, ['date', 'open', 'high', 'low', 'close', 'volume']]


def plot_candle():
    hlines = Hlines.calc_hlines(df, len(df))
    mpf.plot(df, volume=True, style='yahoo', type='candle', mav=[10, 20, 60],
             hlines=dict(hlines=hlines, colors=['r'], linestyle='-.', linewidths=1, alpha=0.8),
             figscale=1.35)


if __name__ == "__main__":
    plot_candle()
