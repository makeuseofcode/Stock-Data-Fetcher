# Importing the yfinance package
import yfinance as yf
ticker = yf.Ticker('GOOGL').info
market_price = ticker['regularMarketPrice']
previous_close_price = ticker['regularMarketPreviousClose']
print('Ticker: GOOGL')
print('Market Price:', market_price)
print('Previous Close Price:', previous_close_price)