import yfinance as yf
import yahoo_fin.stock_info as si
from datetime import datetime, timedelta

"""
    get_analysts_info() 
    get_balance_sheet()
    get_cash_flow()
    get_data()
    get_day_gainers()
    get_day_losers()
    get_day_most_active()
    get_holders()
    get_income_statement()
    get_live_price()
    get_quote_table()
    get_top_crypto()
    get_stats()
    get_stats_valuation()
    tickers_dow()
    tickers_nasdaq()
    tickers_other()
    tickers_sp500()
"""

#
# com_info = si.get_company_info("msft")
# msft = yf.Ticker("MSFT")

# access each ticker using (example)
# print(msft.info)
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
# print(tickers)

# 获取实时价格
# quote = si.get_quote_data('msft')
# print(quote)

# 获取指定股票历史K线 1d 1wk 1mo
# ['open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker']
# msft_data = si.get_data('msft', start_date='01/01/2012', end_date='31/12/2022', interval='1d')

# print(msft_data.columns)
# print(msft_data)


# 获取股票基本信息
# quote_table = si.get_quote_table("aapl", dict_result=False)
# quote_table = si.get_quote_table("eurn", dict_result=False)
# quote_table = si.get_quote_table("baba", dict_result=False)

# print(quote_table)
