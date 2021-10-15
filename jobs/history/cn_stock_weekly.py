
# 导入tushare
import tushare as ts
# 初始化pro接口
pro = ts.pro_api('4896a3e82b65867f1c7ff140dcefe5782b5db55507a5c16b61c24a08')

# 拉取数据
df = pro.weekly(**{
    "ts_code": "",
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

        