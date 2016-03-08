'''
use a base URL to get stock price data from google finance in a nice CSV format
'''
import urllib2
# https://www.google.com/finance/historical?q=NYSE%3AMCD&output=csv
BASE_URL = 'http://www.google.com/finance/historical?'
PARAMS = '&output=csv'  # this URL gets historical data for 1 year by default
stocks = [('BAC', 'NYSE'),('C', 'NYSE'), ('IBM', 'NYSE'), ('AAPL', 'NASDAQ'), ('GE', 'NYSE'), ('T', 'NYSE')]
nyse_stocks = ['BAC', 'C', 'IBM', 'GE', 'T', 'MCD', 'NKE', 'TWTR']
nasdaq_stocks = ['AAPL', 'TSLA']

for stock in nyse_stocks:
    nyse_query = 'q=NYSE%3A'
    company_str = nyse_query + stock
    target_url = BASE_URL + company_str + PARAMS
    data = urllib2.urlopen(target_url)
    filename = 'stock_hourly_data/' + stock + '.csv'
    f = open(filename, 'a')
    for line in data:
        f.write(line)
    print 'got data for', stock
    f.close()

for stock in nasdaq_stocks:
    nasdaq_query = 'q=NASDAQ%3A'
    company_str = nasdaq_query + stock
    target_url = BASE_URL + company_str + PARAMS
    data = urllib2.urlopen(target_url)
    filename = 'stock_hourly_data/' + stock + '.csv'
    f = open(filename, 'a')
    for line in data:
        f.write(line)
    print 'got data for', stock
    f.close()
