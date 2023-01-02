# 导入:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://dev:04f5d5a3b91006a8@121.4.15.211:3306/quant?local_infile=1')
# engine = create_engine('mysql+pymysql://dev:dev123456@8.210.170.98:3306/quant')
# engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine, future=True)
