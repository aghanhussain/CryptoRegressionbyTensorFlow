import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt


def daily_price_historical(symbol, comparison_symbol, all_data=True, limit=1, aggregate=1, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    if all_data:
        url += '&allData=true'
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df

def plotChart(axis,df,symbol,comparison_symbol):
    axis.plot(df.timestamp, df.close)
    axis.set_title(symbol + ' Vs ' + comparison_symbol)
    axis.set_ylabel('Price In ' + comparison_symbol)
    axis.set_xlabel('Year')

df1 = daily_price_historical('BTC','USD')
df2 = daily_price_historical('ETH','USD')
f, axarr = plt.subplots(2)


plotChart(axarr[0],df1,'BTC','USD')
plotChart(axarr[1],df1,'ETH','USD')

plt.show()
