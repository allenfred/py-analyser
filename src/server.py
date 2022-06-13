import time
import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
from jobs.crypto.df import get_inst_df


def message_handler(message):
    print(message)


insts = get_inst_df('biance')
streams = ['!miniTicker@arr']

for index, item in enumerate(insts):
    inst_id = item['instrument_id']
    streams.append(inst_id.lower() + '@kline_15m')
    streams.append(inst_id.lower() + '@kline_1h')

# U本位合约
ws_client = UMFuturesWebsocketClient()
ws_client.start()

# Combine selected streams
ws_client.instant_subscribe(
    # stream=['!miniTicker@arr'],
    stream=streams,
    callback=message_handler,
)
