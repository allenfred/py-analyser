import yfinance as yf
import yahoo_fin.stock_info as si
from datetime import datetime, timedelta

#
# com_info = si.get_company_info("msft")
msft = yf.Ticker("MSFT")

# access each ticker using (example)
print(msft.info)
# print(msft.history(period="1"))
# print(msft.history(start="2012-01-01", end="2022-12-31"))
# print(msft.actions)

# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# data = yf.download('AAPL', start="2022-01-01", end="2022-12-31")

# print(len(data))
# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 标普500指数 成分股
# sp500_tickers = si.tickers_sp500(include_company_data=True)
# print('sp500_tickers ', len(sp500_tickers), ' columns:', sp500_tickers.columns)

# 纳斯达克指数 成分股
# ['Symbol', 'Security Name', 'Market Category', 'Test Issue',
# 'Financial Status', 'Round Lot Size', 'ETF', 'NextShares']
# nasdaq_tickers = si.tickers_nasdaq(include_company_data=True)
# print('other_tickers ', len(nasdaq_tickers), ' columns:', nasdaq_tickers.columns)

# ['ACT Symbol', 'Security Name', 'Exchange', 'CQS Symbol', 'ETF', 'Round Lot Size', 'Test Issue', 'NASDAQ Symbol']
# other_tickers = si.tickers_other(include_company_data=True)
# print('other_tickers ', len(other_tickers), ' columns:', other_tickers.columns)

# 道指 成分股
# tickers = si.tickers_dow()

# 获取实时价格
# quote = si.get_quote_data('msft')

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 获取指定股票历史K线 1d 1wk 1mo
# ['open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker']
msft_data = si.get_data('msft', start_date='01/01/2012', end_date='31/12/2022', interval='1d')

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print(msft_data.columns)
print(msft_data)
# print(splits)
# print(len(tickers))
