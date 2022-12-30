import time
import os
import sys
import redis
import json

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

r = redis.Redis(host='8.210.170.98', port=6371, password='Uwy0Pf8mi', db=0)

from bian.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
from mongo.df import get_instruments
from lib.util import get_timestamp


def message_handler(message):
    print(json.dumps(message))


def jsonDefault(o):
    return o.decode('utf-8')


p = r.pubsub()
p.subscribe('klines')

while True:
    msg = p.get_message()
    if msg is not None:
        # data = json.dumps(msg['data'], default=jsonDefault)
        if type(msg['data']) == bytes:
            data = json.loads(msg['data'])

            # if 'args' in data:
            #     print(data['args'])

            if 'stream' in data and data['stream'] == 'btcusdt@kline_1h':
                print(data['data'])

            # if 'topic' in data:
            #     print(data['topic'])

            # print(json.dumps(data, default=jsonDefault))
            # print(data['stream'])
            # print(msg['data'])
        # data = json.dumps(msg_data)
        # print(msg_data.to_dict())
        #
        # if data.has_key('stream'):
        #     print(data['stream'])

        # if data.has_key('topic'):
        #     print(data)
        #
    # if msg_data.has_key('stream'):
    #     print(msg_data['data'])
    # print(msg)
#
# insts = list(get_instruments('binance'))
# streams = ['btcusdt@kline_1h']
#
# # streams = ['!miniTicker@arr', 'btcusdt@kline_4h']
# #
# # for index, item in enumerate(insts):
# #     inst_id = item['instrument_id']
# #     if len(streams) < 160 and inst_id.endswith('USDT'):
# #         streams.append(inst_id.lower() + '@kline_15m')
# #         streams.append(inst_id.lower() + '@kline_1h')
#
# ws_client = UMFuturesWebsocketClient()
# ws_client.start()
#
# ws_client.instant_subscribe(
#     # stream=['!miniTicker@arr'],
#     stream=streams,
#     callback=message_handler,
# )
#
# print(get_timestamp() + '[Binance] subscriber start...')
