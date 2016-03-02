from pyspark import SparkContext
from os import listdir

if __name__== "__main__":
    sc = SparkContext(appName='StockOutliers')

    files = [ f for f in listdir('./stock-values') if '.txt' in f ]

    print 'Outliers by Company:'
    for f in files:
        rdd = sc.textFile('stock-values/' + f)
        prices = rdd.map(lambda s : float(s))
        stats = prices.stats()
        mean = stats.mean()
        stdev = stats.stdev()

        outliers = prices.filter(lambda p: abs(p - mean) > 2 * stdev)
        print  f + ": " + `outliers.collect()`
