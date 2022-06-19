import os
import sys
from time import sleep

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

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
    # to pass a custom domain in case of connectivity problems, you can use:
    domain="bytick"  # the default is "bybit" 'bytick'
)

# insts = list(get_instruments('bybit'))
# insts = sorted(insts, key=lambda d: d['volume_24h'], reverse=True)
# streams = []
#
# for index, item in enumerate(insts):
#     inst_id = item['instrument_id']
#     if len(streams) < 40 and inst_id.endswith('USDT'):
#         streams.append(inst_id)


def handle_kline(message):
    try:
        if message['data'][0]['confirm']:
            print(message['data'][0])

    except Exception as e:
        print(e)


# print(streams)
# ws.kline_stream(handle_kline, streams, 15)
# ws.kline_stream(handle_kline, streams, 60)

ws.kline_stream(handle_kline, 'BTCUSDT', 15)

while True:
    # This while loop is required for the program to run. You may execute
    # additional code for your trading logic here.
    sleep(1)
