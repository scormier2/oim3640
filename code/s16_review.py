import yfinance as yf



stock = yf.ticker("NVDA")
info = stock.info

#print(info('info.keys())
print(len(info))
print(info['ShortName'])
print(info['currentPrice'])
print(info['currentPrice'])

print(info['longBusinessSummary'])

print(info['longBusinessSummary'].split())

print(info['iPhone' in info['longBusinessSummary'].split()])

print(info['city'])
#info['city'][0] = 'c'
info['city'] = 'Wellesley'
print(info['city'])



#for k, v in info.items():
#    print(k, v)

tickers = ['AAPl', 'MSFT', 'NVDA']
prices = {}
for t in tickers:
    prices[t] = yf.Ticker(t).info['currentPrice']

    price(prices)

    Print(sorted(prices)) #create a new list of the keys in prices, sorted alphabetically
    print(sorted(prices.values(), reverse=True)) #create a new list of the values in prices, sorted from highest to lowest
    print(sorted(prices.keys()))#create a new list of the key-value pairs in prices, sorted by key alphabetically
    
    #how to sort stocks by values, but return the keys in that order?

    #print(tickers)
    print(sum(prices.values()))
          
    Print ={'AAPl': 178.50, 'MSFT': 415.20, 'NVDA': 500.00}
    'MSFT' [375.845, 300]
    print(sum(Prices.values()))

          
    Total = 0
    for prices in prices.values():
        Total += prices
    print(Total)

    tickers.append('GOOG')
    prices(tickers)
    #tickers = {}
    for t in tickers:
        prices[t] = yf.Ticker(t).info['currentPrice']
    print(prices)

    tickers = ['AAPl', 'MSFT', 'NVDA', 'GOOG','META']
    stocks = {} # {NVDA