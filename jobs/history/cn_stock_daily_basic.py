
# 导入tushare
import tushare as ts
# 初始化pro接口
pro = ts.pro_api('4896a3e82b65867f1c7ff140dcefe5782b5db55507a5c16b61c24a08')

# 拉取数据
df = pro.daily_basic(**{
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
    "turnover_rate",
    "turnover_rate_f",
    "volume_ratio",
    "pe",
    "pe_ttm",
    "pb",
    "ps",
    "ps_ttm",
    "dv_ratio",
    "dv_ttm",
    "total_share",
    "float_share",
    "free_share",
    "total_mv",
    "circ_mv",
    "limit_status"
])
print(df)

        