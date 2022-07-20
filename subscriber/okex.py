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
            r.publish('tickers', message)

        if 'candle' in message:
            r.publish('klines', message)

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
                        res = await asyncio.wait_for(ws.recv(), timeout=25)
                    except (
                            asyncio.TimeoutError,
                            websockets.exceptions.ConnectionClosed,
                    ) as e:
                        try:
                            await ws.send("ping")
                            res_b = await ws.recv()
                            continue
                        except Exception as e:
                            timestamp = get_timestamp()
                            print(timestamp + "正在重连……")
                            print(e)
                            break

                    handle_msg(res)

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

                    handle_msg(res)

        except Exception as e:
            time = get_timestamp()
            print(time + "连接断开，正在重连……")
            print(e)
            continue


if __name__ == "__main__":

    api_key = ""
    secret_key = ""
    passphrase = ""

    url = "wss://ws.okx.com:8443/ws/v5/public"
    insts = list(get_instruments())
    insts = sorted(insts, key=lambda d: d['volume_24h'], reverse=True)
    channels = []

    for index, item in enumerate(insts):
        inst_id = item['instrument_id']
        # print(inst_id)

        if len(channels) < 200 and item['exchange'] == 'okex' and item['volume_24h'] > 1000000:
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
