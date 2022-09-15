import yfinance as yf
start_date = '2020-01-01'
end_date = '2022-01-01'

# Add multiple space separated tickers here
ticker = 'GOOGL MSFT TSLA'

data = yf.download(ticker, start_date, end_date)
print(data.tail())