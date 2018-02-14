

import requests


def price(symbol, comparison_symbols=['USD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data
bitcoin=price('BTC')
ethereum=price('ETH')

print( "Bit Coin", bitcoin['USD'])
print( "Ethereum", ethereum['USD'])
