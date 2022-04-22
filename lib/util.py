from talib import SMA, EMA, MACD
from lib.quota.bias import bias
from lib.quota.ma_slope import slope
from lib.quota.magic_nine_turn import td
import platform


def is_mac_os():
    system_p = platform.platform()
    if "macOS" in system_p:
        return True
    else:
        return False


def used_time_fmt(start, end):
    seconds = int(end - start)
    if seconds > 3600:
        return str(seconds // 3600) + ' h ' + str((seconds - (3600 * (seconds // 3600))) // 60) + \
               ' min ' + str(seconds % 60) + ' s'
    if 60 < seconds < 3600:
        return str(seconds // 60) + ' min ' + str(int(seconds % 60)) + ' s'
    return str(round(end - start, 1)) + ' s'


def set_quota(df):
    close = df.close.to_numpy()

    df['ma5'] = SMA(close, 5)
    df['ma10'] = SMA(close, 10)
    df['ma20'] = SMA(close, 20)
    df['ma30'] = SMA(close, 30)
    df['ma34'] = SMA(close, 34)
    df['ma55'] = SMA(close, 55)
    df['ma60'] = SMA(close, 60)
    df['ma120'] = SMA(close, 120)
    df['ma144'] = SMA(close, 144)
    df['ma169'] = SMA(close, 169)

    df['ema5'] = EMA(close, 5)
    df['ema10'] = EMA(close, 10)
    df['ema20'] = EMA(close, 20)
    df['ema30'] = EMA(close, 30)
    df['ema34'] = EMA(close, 34)
    df['ema55'] = EMA(close, 55)
    df['ema60'] = EMA(close, 60)
    df['ema120'] = EMA(close, 120)
    df['ema144'] = EMA(close, 144)
    df['ema169'] = EMA(close, 169)
    df['ema288'] = EMA(close, 288)
    df['ema338'] = EMA(close, 338)
    df['ema576'] = EMA(close, 576)
    df['ema676'] = EMA(close, 676)

    df['ma5_slope'] = slope(close, 'SMA', 5)
    df['ma10_slope'] = slope(close, 'SMA', 10)
    df['ma20_slope'] = slope(close, 'SMA', 20)
    df['ma30_slope'] = slope(close, 'SMA', 30)
    df['ma34_slope'] = slope(close, 'SMA', 34)
    df['ma55_slope'] = slope(close, 'SMA', 55)
    df['ma60_slope'] = slope(close, 'SMA', 60)
    df['ma72_slope'] = slope(close, 'SMA', 72)
    df['ma120_slope'] = slope(close, 'SMA', 120)
    df['ma144_slope'] = slope(close, 'SMA', 144)
    df['ma169_slope'] = slope(close, 'SMA', 169)

    df['ema5_slope'] = slope(close, 'EMA', 5)
    df['ema10_slope'] = slope(close, 'EMA', 10)
    df['ema20_slope'] = slope(close, 'EMA', 20)
    df['ema30_slope'] = slope(close, 'EMA', 30)
    df['ema34_slope'] = slope(close, 'EMA', 34)
    df['ema55_slope'] = slope(close, 'EMA', 55)
    df['ema60_slope'] = slope(close, 'EMA', 60)
    df['ema120_slope'] = slope(close, 'EMA', 120)
    df['ema144_slope'] = slope(close, 'EMA', 144)
    df['ema169_slope'] = slope(close, 'EMA', 169)
    df['ema288_slope'] = slope(close, 'EMA', 288)
    df['ema338_slope'] = slope(close, 'EMA', 338)
    df['ema576_slope'] = slope(close, 'EMA', 576)
    df['ema676_slope'] = slope(close, 'EMA', 676)

    DIFF, DEA, MACD_BAR = MACD(close)

    df['diff'] = DIFF
    df['dea'] = DEA
    df['macd'] = MACD_BAR

    bias6, bias12, bias24, bias55, bias60, bias72, bias120 = bias(close)
    df['bias6'] = bias6
    df['bias12'] = bias12
    df['bias24'] = bias24
    df['bias55'] = bias55
    df['bias60'] = bias60
    df['bias72'] = bias72
    df['bias120'] = bias120

    high_td, low_td = td(close)
    df['high_td'] = high_td
    df['low_td'] = low_td

    df = df.fillna(0)

    return df
