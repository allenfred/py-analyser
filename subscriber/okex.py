import time
import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
from mongo.df import get_instrument_ticker


def message_handler(message):
    print(message)


insts = list(get_instrument_ticker('okex'))
insts = sorted(insts, key=lambda d: d['volume_24h'], reverse=True)
streams = ['!miniTicker@arr']

for index, item in enumerate(insts):
    inst_id = item['instrument_id']
    if index < 70:
        print(inst_id)
        streams.append(inst_id.lower() + '@kline_15m')
        streams.append(inst_id.lower() + '@kline_1h')
#
# ws_client = UMFuturesWebsocketClient()
# ws_client.start()
#
# ws_client.instant_subscribe(
#     # stream=['!miniTicker@arr'],
#     stream=streams,
#     callback=message_handler,
# )

print('Okex subscriber start...')
