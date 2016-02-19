from tweepy.streaming import StreamListener
import json
import time

# Companies to filter with
keywords = ['facebook', 'google', 'amazon', 'microsoft', 'twitter', 'linkedin', 'apple']

class StreamTweetListener(StreamListener):
    def __init__(self):
        self.start = time.time()
        self.end = 1800

    def on_data(self, tweet):
        if time.time() - self.start <= self.end:
            json_tweet = json.loads(tweet)
            try:
                if json_tweet['lang'] == 'en':
                    # Finding and Storing keywords
                    text = json_tweet['text'].lower().encode('ascii','ignore')
                    companies = [keyword for keyword in keywords if keyword in text]
                    for company in companies:
                        print json_tweet['text'], 'Company: ', company
                        filename = 'twitter-docs/' + company + '.txt'
                        f = open(filename, 'a') # append option
                        f.write(text + '\n')
                        f.close()
            except:
                pass
        else:
            self.on_error('30 mins up')

    def on_error(self, status):
        print "Error: "+ status + "\n"
        return False

    def on_status(self, status):
        print "Status: ", status
