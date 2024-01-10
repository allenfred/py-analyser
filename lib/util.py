from talib import SMA, EMA, MACD, ATR, LINEARREG_SLOPE
import talib as lib
import platform
import datetime
import numpy as np

import matplotlib.pyplot as plt
from lib.quota.bias import bias
from lib.quota.ma_slope import slope
from lib.quota.magic_nine_turn import td


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


def decimal_digits(val: float):
    val_str = str(val)
    digits_location = val_str.find('.')

    if digits_location:
        return len(val_str[digits_location + 1:])


def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return "[" + t + "Z" + "]"


def set_quota(df):
    df = df.astype({"open": 'float', "high": 'float', "low": 'float', "close": 'float'})

    open = df.open.to_numpy()
    high = df.high.to_numpy()
    low = df.low.to_numpy()
    close = df.close.to_numpy()
    vol = np.array(df.vol.to_numpy(), dtype='f8')

    df['vol5'] = SMA(vol, 5)
    df['vol10'] = SMA(vol, 10)
    df['vol20'] = SMA(vol, 20)
    df['vol30'] = SMA(vol, 30)

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

    df['atr'] = ATR(high, low, close, timeperiod=14)
    # 振幅
    pct_range = []
    for index in range(len(df)):
        chg = 0
        if index > 0:
            chg = round(((df.iloc[index]['high'] - df.iloc[index]['low']) / df.iloc[index - 1]['close']) * 100, 2)
        pct_range.insert(index, chg)
    df['pct_range'] = pct_range

    df = df.fillna(0)
    df = df.round(max([decimal_digits(min(open)), decimal_digits(min(high)),
                       decimal_digits(min(low)), decimal_digits(min(close))]) + 1)

    return df


def is_smile_curve(ma60):
    # check if the input is a list of numbers
    if not isinstance(ma60, list) or not all(isinstance(x, (int, float)) for x in ma60):
        print("Invalid input. Please provide a list of numbers.")
        return None

    # convert the list to a numpy array
    ma60 = np.array(ma60)

    # calculate the mean and standard deviation of the array
    mean = np.mean(ma60)
    std = np.std(ma60)

    # define a threshold for the smile curve
    # this can be adjusted according to your preference
    threshold = 0.1 * std

    # check if the first and last values are above the mean by the threshold
    if ma60[0] > mean + threshold and ma60[-1] > mean + threshold:
        # check if the middle value is below the mean by the threshold
        if ma60[len(ma60) // 2] < mean - threshold:
            # plot the array and show the smile curve
            plt.plot(ma60)
            plt.title("Smile Curve")
            plt.xlabel("Days")
            plt.ylabel("Moving Average")
            plt.show()
            print("Yes, the moving average is looking like a smile curve.")
            return True

    # plot the array and show the non-smile curve
    plt.plot(ma60)
    plt.title("Non-Smile Curve")
    plt.xlabel("Days")
    plt.ylabel("Moving Average")
    plt.show()
    print("No, the moving average is not looking like a smile curve.")
    return False
