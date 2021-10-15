
# 导入tushare
import tushare as ts
# 初始化pro接口
pro = ts.pro_api('4896a3e82b65867f1c7ff140dcefe5782b5db55507a5c16b61c24a08')

# 拉取数据
df = pro.index_basic(**{
    "ts_code": "",
    "market": "",
    "publisher": "",
    "category": "",
    "name": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "name",
    "market",
    "publisher",
    "category",
    "base_date",
    "base_point",
    "list_date",
    "desc",
    "index_type",
    "fullname",
    "exp_date"
])
print(df.name)

        