import pandas as pd
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries

#unique api key from alphavantage website
API_key = 'YCW41DVHFHMIOFMX'

#list of stock companies in DOW 30
symbols = ["WMT", "TSLA", "BA", "AAPL"]

stock_sheets = ["WMT.xlsx", "TSLA.xlsx", "BA.xlsx", "AAPL.xlsx"]

ts = TimeSeries(key='API_key', output_format='pandas')
j = 1

while j==1:
    for i in range (len(symbols)):
        data, meta_data = ts.get_intraday(symbol=symbols[i], interval='1min', outputsize='full')
        print(data)
        data.to_excel(stock_sheets[i])
        close_data = data['4. close']
        percent_change = close_data.pct_change()
        percent_change.to_csv("pctchange.text")

        lastval_change = percent_change[-1]

    i = i+1


