'''
use a base URL to get stock price data from google finance in a nice CSV format
'''
import urllib2

BASE_URL = 'http://www.google.com/finance/getprices?'
PARAMS = '&i=3600&p=1M&f=d,o,c,v' # gets opening & closing stock price
                                         # every hour for 1 month
stocks = [('BAC', 'NYSE'),('C', 'NYSE'), ('IBM', 'NYSE'), ('AAPL', 'NASDAQ'), ('GE', 'NYSE'), ('T', 'NYSE')]
nyse_stocks = ['BAC', 'C', 'IBM', 'GE', 'T', 'MCD', 'NKE', 'TWTR']
nasdaq_stocks = ['AAPL', 'TSLA']

for stock in nyse_stocks:
    # q=AAPL&x=NASDAQ
    company_str = 'q=' + stock
    exchange = '&x=' + 'NYSE'
    target_url = BASE_URL + company_str + exchange + PARAMS
    data = urllib2.urlopen(target_url)
    filename = 'stock_hourly_data/' + stock + '.txt'
    f = open(filename, 'a')
    for line in data:
        f.write(line)
    print 'got data for ', stock
    f.close()

for stock in nasdaq_stocks:
    # q=AAPL&x=NASDAQ
    company_str = 'q=' + stock
    exchange = '&x=' + 'NASD'
    target_url = BASE_URL + company_str + exchange + PARAMS
    data = urllib2.urlopen(target_url)
    filename = 'stock_hourly_data/' + stock + '.txt'
    f = open(filename, 'a')
    for line in data:
        f.write(line)
    print 'got data for ', stock
    f.close()
