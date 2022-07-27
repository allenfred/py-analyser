import os
import sys
import redis
from time import sleep
import json

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

r = redis.Redis(host='8.210.170.98', port=6371, password='Uwy0Pf8mi', db=0)

"""
To see which endpoints and topics are available, check the Bybit API
documentation: https://bybit-exchange.github.io/docs/inverse/#t-websocket
There are several WSS URLs offered by Bybit, which pybit manages for you.
However, you can set a custom `domain` as shown below.
"""
from pybit import usdt_perpetual
from mongo.df import get_instruments
from lib.util import get_timestamp

ws = usdt_perpetual.WebSocket(
    test=False,
    api_key=None,  # omit the api_key & secret to connect w/o authentication
    api_secret=None,
    # ping_interval=30,  # the default is 30
    # ping_timeout=10,  # the default is 10
    # to pass a custom domain in case of connectivity problems, you can use:
    domain="bybit"  # the default is "bybit" 'bytick'
)

insts = list(get_instruments())
insts = sorted(insts, key=lambda d: d['volume_24h'], reverse=True)
kline_streams = []
ticker_streams = []

for index, item in enumerate(insts):
    inst_id = item['instrument_id']
    if len(kline_streams) < 20 and item['exchange'] == 'bybit' and \
            inst_id.endswith('USDT') and item['volume_24h'] > 1000000:
        kline_streams.append(inst_id)
        ticker_streams.append(inst_id)


def handle_kline(message):
    try:
        r.publish('klines', json.dumps(message))
    except Exception as e:
        print(e)


def handle_ticker(message):
    r.publish('tickers', json.dumps(message))


ws.instrument_info_stream(handle_ticker, ticker_streams)
ws.kline_stream(handle_kline, kline_streams, 15)
ws.kline_stream(handle_kline, kline_streams, 60)
ws.kline_stream(handle_kline, ['BTCUSDT'], 240)

print(get_timestamp() + '[Bybit] subscriber start...')

while True:
    # This while loop is required for the program to run. You may execute
    # additional code for your trading logic here.
    sleep(1)


