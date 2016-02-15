from pyspark import SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF
import re

if __name__ == '__main__':
    sc = SparkContext(appName='WikipediaTFIDF')

    npc_problems = sc.wholeTextFiles('wiki-pages/').values().map(lambda doc : re.split('\W+', doc))

    # get tf-idf values for each np-complete problem
    tf = HashingTF().transform(npc_problems)
    idf = IDF().fit(tf)
    tfidf = idf.transform(tf)
    tfidf.saveAsTextFile('wikipedia-tfidf-output')
