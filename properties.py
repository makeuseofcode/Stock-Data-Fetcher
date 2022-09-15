# Importing the yfinance package
import yfinance as yf
ticker = yf.Ticker('GOOGL').info
print(ticker.keys())