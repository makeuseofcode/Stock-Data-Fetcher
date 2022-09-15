import yfinance as yf
start_date = '2020-01-01'
end_date = '2022-01-01'
ticker = 'GOOGL'
data = yf.download(ticker, start_date, end_date)

data["Date"] = data.index
data = data[["Date", "Open", "High", 
             "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
print(data.head())