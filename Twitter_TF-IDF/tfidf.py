from pyspark import SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF
import re

if __name__ == '__main__':
    sc = SparkContext(appName='TwitterTFIDF')
    # sc.wholeTextFiles() gives (key, value) pairs
    # I only need the values (content of the file)
    # then split the contents of the files by word
    company_tweets = sc.wholeTextFiles('twitter-docs/').values().map(lambda doc : re.split('\W+',doc))

    # get tf-idf values for each company
    tf = HashingTF().transform(company_tweets)
    idf = IDF().fit(tf)
    tfidf = idf.transform(tf)
    tfidf.saveAsTextFile('twitter-tfidf-output')
