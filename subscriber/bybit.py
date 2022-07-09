import os
import sys
import redis
from time import sleep
import json

path = os.path.dirname(os.path.abspath(__file__))
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

ws = usdt_perpetual.WebSocket(
    test=False,
    api_key=None,  # omit the api_key & secret to connect w/o authentication
    api_secret=None,
    # ping_interval=30,  # the default is 30
    # ping_timeout=10,  # the default is 10
    # to pass a custom domain in case of connectivity problems, you can use:
    domain="bybit"  # the default is "bybit" 'bytick'
)

insts = list(get_instruments('bybit'))
insts = sorted(insts, key=lambda d: d['volume_24h'], reverse=True)
streams = []

for index, item in enumerate(insts):
    inst_id = item['instrument_id']
    if len(streams) < 20 and inst_id.endswith('USDT'):
        streams.append(inst_id)


def handle_kline(message):
    try:
        r.publish('klines', json.dumps(message))
    except Exception as e:
        print(e)


ws.kline_stream(handle_kline, streams, 15)
ws.kline_stream(handle_kline, streams, 60)
ws.kline_stream(handle_kline, ['BTCUSDT'], 240)

print('[Bybit] subscriber start...')

while True:
    # This while loop is required for the program to run. You may execute
    # additional code for your trading logic here.
    sleep(1)


