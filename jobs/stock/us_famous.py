import akshare as ak

if __name__ == "__main__":
    stock_us_famous_spot_em_df = ak.stock_us_famous_spot_em(symbol='科技类')
    print(stock_us_famous_spot_em_df)
    print(len(stock_us_famous_spot_em_df))