import yfinance as yf
start_date = '2020-01-01'
end_date = '2022-01-01'
ticker = 'GOOGL'
data = yf.download(ticker, start_date, end_date)
print(data.tail())

# Export data to a CSV file
data.to_csv("GOOGL.csv")