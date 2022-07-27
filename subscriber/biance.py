import time
import os
import sys
import redis
import json

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

r = redis.Redis(host='8.210.170.98', port=6371, password='Uwy0Pf8mi', db=0)

from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
from mongo.df import get_instruments
from lib.util import get_timestamp


def message_handler(message):
    if message['stream'].find('miniTicker') > 0:
        r.publish('tickers', json.dumps(message))

    if message['stream'].find('kline') > 0:
        r.publish('klines', json.dumps(message))


insts = list(get_instruments('biance'))
insts = sorted(insts, key=lambda d: d['volume_24h'], reverse=True)
streams = ['!miniTicker@arr', 'btcusdt@kline_4h']

for index, item in enumerate(insts):
    inst_id = item['instrument_id']
    if len(streams) < 160 and inst_id.endswith('USDT'):
        streams.append(inst_id.lower() + '@kline_15m')
        streams.append(inst_id.lower() + '@kline_1h')

ws_client = UMFuturesWebsocketClient()
ws_client.start()

ws_client.instant_subscribe(
    # stream=['!miniTicker@arr'],
    stream=streams,
    callback=message_handler,
)

print(get_timestamp() + '[Biance] subscriber start...')
