import pandas as pd
import numpy as np
import mplfinance as mpf
import matplotlib.dates as mpl_dates
from sqlalchemy import text
from klines import get_stock_klines, get_crypto_klines

#
# from models.cn_daily_candles import CNDailyCandleDao
#
# dailyCandleDao = CNDailyCandleDao()
#
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
# statement = dailyCandleDao.session.execute(
#     text("select trade_date, open, high, close, low, pct_chg, amount*1000 as volume "
#          "from "
#          + "cn_daily_candles" + " where ts_code = :ts_code "
#          + "and trade_date > '2020-01-01' and open is not null "
#            "and close is not null and high is not null and"
#          + " low is not null "
#          + "order by trade_date desc "
#            "limit 250").params(ts_code=ts_code))
#
# kline_df = pd.DataFrame(statement.fetchall(), columns=['trade_date', 'open', 'high', 'close',
#                                                        'low', 'pct_chg', 'volume'])

#
# df = kline_df
# df = df.sort_values(by='trade_date', ascending=True)
# df['date'] = pd.to_datetime(df.trade_date)
# df = df.set_index('date')
# df['date'] = df['trade_date'].apply(mpl_dates.date2num)
#
# df = df.loc[:, ['date', 'open', 'high', 'low', 'close', 'volume']]

# df = get_stock_klines(ts_code)

gran = 3600
exchange = 'binance'
inst_id = 'ETHUSDT'
inst_id = 'DYDXUSDT'
inst_id = 'STORJUSDT'
inst_id = 'RLCUSDT'
inst_id = 'CRVUSDT'
# inst_id = 'CTSIUSDT'
inst_id = 'OCEANUSDT'

df = get_crypto_klines(exchange, inst_id, gran, 300)


def is_support(df, i):
    support = df['low'][i] < df['low'][i - 1] < df['low'][i - 2] and \
              df['low'][i] < df['low'][i + 1] < df['low'][i + 2]

    return support


def is_resistance(df, i):
    resistance = df['high'][i] > df['high'][i - 1] > df['high'][i - 2] and \
                 df['high'][i] > df['high'][i + 1] > df['high'][i + 2]

    return resistance


# volatility 波动率
s = np.mean(df['high'] - df['low'])


def is_far_from_level(l):
    return np.sum([abs(l - x) < s for x in levels]) == 0


levels = []
hlines = []

for i in range(2, df.shape[0] - 2):
    if is_support(df, i):
        l = df['low'][i]

        if is_far_from_level(l):
            levels.append((i, l))
            hlines.append(l)

    elif is_resistance(df, i):
        l = df['high'][i]

        if is_far_from_level(l):
            levels.append((i, l))
            hlines.append(l)


def plot_candle():
    mpf.plot(df, volume=True, style='yahoo', type='candle', mav=[10, 20, 60],
             hlines=dict(hlines=hlines, colors=['r'], linestyle='-.', linewidths=1, alpha=0.8),
             figscale=1.35)


if __name__ == "__main__":
    plot_candle()
