# 导入:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接:
# engine = create_engine('mysql+pymysql://dev:dev123456@8.210.170.98:3306/quant')
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine, future=True)
