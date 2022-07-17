import os
import sys
import asyncio
import websockets
import json
import requests
import dateutil.parser as dp
import hmac
import base64
import datetime
import redis

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from mongo.df import get_instruments

r = redis.Redis(host='8.210.170.98', port=6371, password='Uwy0Pf8mi', db=0)


def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"


def get_server_time():
    url = "https://www.okx.com/api/general/v3/time"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["iso"]
    else:
        return ""


def server_timestamp():
    server_time = get_server_time()
    parsed_t = dp.parse(server_time)
    timestamp = parsed_t.timestamp()
    return timestamp


def login_params(timestamp, api_key, passphrase, secret_key):
    message = timestamp + "GET" + "/users/self/verify"

    mac = hmac.new(
        bytes(secret_key, encoding="utf8"),
        bytes(message, encoding="utf-8"),
        digestmod="sha256",
    )
    d = mac.digest()
    sign = base64.b64encode(d)

    login_param = {
        "op": "login",
        "args": [api_key, passphrase, timestamp, sign.decode("utf-8")],
    }
    login_str = json.dumps(login_param)
    return login_str


def sort_num(n):
    if n.isdigit():
        return int(n)
    else:
        return float(n)


def change(num_old):
    num = pow(2, 31) - 1
    if num_old > num:
        out = num_old - num * 2 - 2
    else:
        out = num_old
    return out


def handle_msg(message):
    try:
        if 'tickers' in message:
            r.publish('tickers', json.dumps(message))

        if 'candle' in message:
            r.publish('klines', json.dumps(message))

    except Exception as e:
        print(e)


# subscribe channels un_need login
async def subscribe_without_login(url, channels):
    l = []
    while True:
        try:
            async with websockets.connect(url) as ws:
                sub_param = {"op": "subscribe", "args": channels}
                sub_str = json.dumps(sub_param)
                await ws.send(sub_str)

                while True:
                    try:
                        res_b = await asyncio.wait_for(ws.recv(), timeout=25)
                    except (
                            asyncio.TimeoutError,
                            websockets.exceptions.ConnectionClosed,
                    ) as e:
                        try:
                            await ws.send("ping")

                            res_b = await ws.recv()
                            timestamp = get_timestamp()
                            print(timestamp + res_b)
                            continue
                        except Exception as e:
                            timestamp = get_timestamp()
                            print(timestamp + "正在重连……")
                            print(e)
                            break

                    timestamp = get_timestamp()

                    print(timestamp + res_b)

        except Exception as e:
            timestamp = get_timestamp()
            print(timestamp + "连接断开，正在重连……")
            print(e)
            continue


# subscribe channels need login
async def subscribe(url, api_key, passphrase, secret_key, channels):
    while True:
        try:
            async with websockets.connect(url) as ws:
                # login
                timestamp = str(server_timestamp())
                login_str = login_params(timestamp, api_key, passphrase, secret_key)
                await ws.send(login_str)
                time = get_timestamp()
                print(time + f"send: {login_str}")
                res = await ws.recv()
                time = get_timestamp()
                print(time + res)

                # subscribe
                sub_param = {"op": "subscribe", "args": channels}
                sub_str = json.dumps(sub_param)
                await ws.send(sub_str)
                time = get_timestamp()
                print(time + f"send: {sub_str}")

                while True:
                    try:
                        res = await asyncio.wait_for(ws.recv(), timeout=25)
                    except (
                            asyncio.TimeoutError,
                            websockets.exceptions.ConnectionClosed,
                    ) as e:
                        try:
                            await ws.send("ping")
                            res_b = await ws.recv()
                            time = get_timestamp()
                            print(time + res_b)
                            continue
                        except Exception as e:
                            time = get_timestamp()
                            print(time + "正在重连……")
                            print(e)
                            break
                    print(res)
                    # handle_kline(res)

        except Exception as e:
            time = get_timestamp()
            print(time + "连接断开，正在重连……")
            print(e)
            continue


# unsubscribe channels
async def unsubscribe(url, api_key, passphrase, secret_key, channels):
    async with websockets.connect(url) as ws:
        # login
        timestamp = str(server_timestamp())
        login_str = login_params(str(timestamp), api_key, passphrase, secret_key)
        await ws.send(login_str)
        time = get_timestamp()
        print(time + f"send: {login_str}")

        res = await ws.recv()
        time = get_timestamp()
        print(time + res)

        # unsubscribe
        sub_param = {"op": "unsubscribe", "args": channels}
        sub_str = json.dumps(sub_param)
        await ws.send(sub_str)
        time = get_timestamp()
        print(time + f"send: {sub_str}")

        res = await ws.recv()
        time = get_timestamp()
        print(time + res)


# unsubscribe channels
async def unsubscribe_without_login(url, channels, timestamp):
    async with websockets.connect(url) as ws:
        # unsubscribe
        sub_param = {"op": "unsubscribe", "args": channels}
        sub_str = json.dumps(sub_param)
        await ws.send(sub_str)
        print(timestamp + f"send: {sub_str}")

        res = await ws.recv()
        print(timestamp + f"recv: {res}")


if __name__ == "__main__":

    api_key = ""
    secret_key = ""
    passphrase = ""

    url = "wss://ws.okx.com:8443/ws/v5/public"

    # 现货
    # 用户币币账户频道
    # channels = ["spot/account:USDT"]
    # 用户杠杆账户频道
    # channels = ["spot/margin_account:BTC-USDT"]
    # 用户委托策略频道
    # channels = ["spot/order_algo:BTC-USDT"]
    # 用户交易频道
    # channels = ["spot/order:BTC-USDT"]
    # 公共-Ticker频道
    # channels = ["spot/ticker:BTC-USDT"]
    # 公共-K线频道
    # channels = ["spot/candle60s:BTC-USDT"]
    # 公共-交易频道
    # channels = ["spot/trade:BTC-USDT"]
    # 公共-5档深度频道
    # channels = ["spot/depth5:BTC-USDT"]
    # 公共-400档深度频道
    # channels = ["spot/depth:BTC-USDT"]
    # 公共-400档增量数据频道
    # channels = ["spot/depth_l2_tbt:BTC-USDT"]

    # 交割合约
    # 用户持仓频道
    # channels = ["futures/position:BTC-USD-200327"]
    # 用户账户频道
    # channels = ["futures/account:BTC"]
    # 用户交易频道
    # channels = ["futures/order:BTC-USD-200626"]
    # 用户委托策略频道
    # channels = ["futures/order_algo:BTC-USD-200327"]
    # 公共-全量合约信息频道
    # channels = ["futures/instruments"]
    # 公共-Ticker频道
    # channels = ["futures/ticker:BTC-USD-200626"]
    # 公共-K线频道
    # channels = ["futures/candle60s:BTC-USD-200626"]
    # 公共-交易频道
    # channels = ["futures/trade:BTC-USD-200117"]
    # 公共-预估交割价频道
    # channels = ["futures/estimated_price:BTC-USD-200228"]
    # 公共-限价频道
    # channels = ["futures/price_range:BTC-USD-200327"]
    # 公共-5档深度频道
    # channels = ["futures/depth5:BTC-USD-200327"]
    # 公共-400档深度频道
    # channels = ["futures/depth:BTC-USD-200327"]
    # 公共-400档增量数据频道
    # channels = ["futures/depth_l2_tbt:BTC-USD-200327"]
    # 公共-标记价格频道
    # channels = ["futures/mark_price:BTC-USD-200327"]

    # 永续合约
    # 用户持仓频道
    # channels = ["swap/position:BTC-USD-SWAP"]
    # 用户账户频道
    # channels = ["swap/account:BTC-USD-SWAP"]
    # 用户交易频道
    # channels = ["swap/order:BTC-USD-SWAP"]
    # 用户委托策略频道
    # channels = ["swap/order_algo:BTC-USD-SWAP"]
    # 公共-Ticker频道
    # channels = ["swap/ticker:BTC-USD-SWAP"]
    # 公共-K线频道
    # channels = ["swap/candle60s:BTC-USDT-SWAP"]
    # 公共-交易频道
    # channels = ["swap/trade:BTC-USD-SWAP"]
    # 公共-资金费率频道
    # channels = ["swap/funding_rate:BTC-USD-SWAP"]
    # 公共-限价频道
    # channels = ["swap/price_range:BTC-USD-SWAP"]
    # 公共-5档深度频道
    # channels = ["swap/depth5:BTC-USD-SWAP"]
    # 公共-400档深度频道
    # channels = ["swap/depth:BTC-USDT-SWAP"]
    # 公共-400档增量数据频道
    # channels = ["swap/depth_l2_tbt:BTC-USD-SWAP"]
    # 公共-标记价格频道
    # channels = ["swap/mark_price:BTC-USD-SWAP"]

    # 期权合约
    # 用户持仓频道
    # channels = ["option/position:BTC-USD"]
    # 用户账户频道
    # channels = ["option/account:BTC-USD"]
    # 用户交易频道
    # channels = ["option/order:BTC-USD"]
    # 公共-合约信息频道
    # channels = ["option/instruments:BTC-USD"]
    # 公共-期权详细定价频道
    # channels = ["option/summary:BTC-USD"]
    # 公共-K线频道
    # channels = ["option/candle60s:BTC-USD-200327-11000-C"]
    # 公共-最新成交频道
    # channels = ["option/trade:BTC-USD-200327-11000-C"]
    # 公共-Ticker频道
    # channels = ["option/ticker:BTC-USD-200327-11000-C"]
    # 公共-5档深度频道
    # channels = ["option/depth5:BTC-USD-200327-11000-C"]
    # 公共-400档深度频道
    # channels = ["option/depth:BTC-USD-200327-11000-C"]
    # 公共-400档增量数据频道
    # channels = ["option/depth_l2_tbt:BTC-USD-200327-11000-C"]

    # ws公共指数频道
    # 指数行情
    # channels = ["index/ticker:BTC-USD"]
    # 指数K线
    # channels = ["index/candle60s:BTC-USDT"]

    # WebSocket-获取系统升级状态
    # channels = ["system/status"]

    insts = list(get_instruments())
    insts = sorted(insts, key=lambda d: d['volume_24h'], reverse=True)
    channels = []

    for index, item in enumerate(insts):
        inst_id = item['instrument_id']
        if len(channels) < 200 and item['exchange'] == 'okex':
            channels.append({
                "channel": "candle15m",
                "instId": inst_id
            })

            channels.append({
                "channel": "candle1H",
                "instId": inst_id
            })

            channels.append({
                "channel": "tickers",
                "instId": inst_id
            })

    loop = asyncio.get_event_loop()

    # 公共数据 不需要登录（行情，K线，交易数据，资金费率，限价范围，深度数据，标记价格等频道）
    loop.run_until_complete(subscribe_without_login(url, channels))

    # 个人数据 需要登录（用户账户，用户交易，用户持仓等频道）
    # loop.run_until_complete(subscribe(url, api_key, passphrase, secret_key, channels))

    # loop.close()
