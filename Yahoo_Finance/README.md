# Yahoo Finance Outlier Detection

###Steps

1. Use the `yahoo-finance` api to obtain stock data of a list of companies. Company
symbols are needed obtain the company's stock data.

  ```python
  from yahoo_finance import Share

  symbols = ['LNKD', 'GOOG', 'FB', 'MSFT', 'AMZN']
  company_names = ['LinkedIn', 'Google', 'Facebook', 'Microsoft', 'Amazon']

  # Holds the yahoo-finance object for all companies
  companies = []

  for symbol in symbols:
      companies.append(Share(symbol))
  ```

2. Obtain company stock price in intervals of one minute for 30 minutes. Store
these values on a new line in separate files. These files are stored inside a
folder named `Stock-Prices`.

  ```python
  def get_current_price(companies, company_names):
      for i, company in enumerate(companies):
          company.refresh()
          price = company.get_price()
          print company.symbol + ' ' + `price`

          # Store the price in separate text files.
          with open('Stock-Prices/' + company_names[i] + '_shares.txt', 'a') as f:
              f.write(price + '\n')

  start_time = time.time()
  count = 0

  while count < 30:
      get_current_price(companies, company_names)
      print ''
      count += 1
      # intervals of 1 min
      time.sleep(60)
  ```

3. Create separate RDDs for each company's stock data.

  ```python
  from os import listdir

  files = [ f for f in listdir('./Stock-Prices') if '.txt' in f ]
  for f in files:
      rdd = sc.textFile("Stock-Prices/" + f)
  ```

4. Prices in each line of the RDD are in string format. We need to convert them
to float type.

  ```python
  prices = rdd.map(lambda s : float(s))
  ```

5. We now find the mean and standard deviation of the stock prices for each company.

  ```python
  mean = prices.mean()
  stdev = prices.stdev()
  ```

6. To find the outliers we see if the difference between any value and the mean
is greater than twice the standard deviation.

  ```python
  outliers = prices.filter(lambda p: abs(p - mean) > 2 * stdev)
  ```
7. And finally print the outliers

  ```python
  print "Outliers in " + f[:len(f)-4] + ": " + `outliers.collect()`
  ```

8. Final output...
  ```
  Outliers in LinkedIn_shares: [102.49, 102.49]
  Outliers in Microsoft_shares: [49.1]
  Outliers in Facebook_shares: []
  Outliers in Amazon_shares: [506.7, 506.7]
  Outliers in Google_shares: []
  ```
