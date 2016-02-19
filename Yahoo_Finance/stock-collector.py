from yahoo_finance import Share
import time

symbols = ['LNKD', 'GOOG', 'FB', 'MSFT', 'AMZN']
company_names = ['LinkedIn', 'Google', 'Facebook', 'Microsoft', 'Amazon']
companies = []

for symbol in symbols:
    companies.append(Share(symbol))

def get_current_price(companies, company_names):
    for i, company in enumerate(companies):
        company.refresh()
        price = company.get_price()
        print company.symbol + ' ' + `price`

        with open('stock-values/' + company_names[i] + '_shares.txt', 'a') as f:
            f.write(price + '\n')

start_time = time.time()
count = 0

while count < 30:
    get_current_price(companies, company_names)
    print ''
    count += 1
    time.sleep(60)
