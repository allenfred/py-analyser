import tushare as ts
from config.common import TS_TOKEN

pro = ts.pro_api(TS_TOKEN)

df = pro.index_weekly(**{
    "ts_code": "000001.SH",
    "trade_date": "",
    "start_date": "",
    "end_date": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "trade_date",
    "close",
    "open",
    "high",
    "low",
    "pre_close",
    "change",
    "pct_chg",
    "vol",
    "amount"
])
print(df)

                