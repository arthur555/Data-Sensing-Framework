#!/usr/bin/env python3
import tweepy
consumer_key = 'jitZgZzkD42PETiW4hz3QvA5z'
consumer_secret = 'OXqH4zvkFNGrtiSekTI5vcj4gehK0WhtKGzi4Oz3c0y4odBZ9H'

access_token_key = '1872893581-ZphrbUVBpXfKSnMBw935UcJTZ84tW1uNejERGYz'
access_token_secret = 'CD6uyPVIixdnO5jexw7opfWnwwD5rwKW7W5eUoZu4hJLR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, callback):
        tweepy.StreamListener.__init__(self)
        self.callback = callback

    def on_status(self, status):
        self.callback(status)
        return False

def getATweet(callback, word):
    stream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(callback))
    stream.filter(track=[word])

def getData(listt):
    for status in tweepy.Cursor(api.home_timeline).items(10):
        # Process a single status
        dictt = status._json
        listt.append( dictt['text'])
        listt.append (dictt['user']['name'])
        listt.append (dictt['created_at'])
    
if __name__ == '__main__':
    def callbackMethod(tweet):
        print(tweet.text)
#    getATweet(callbackMethod, "hello")

    for status in tweepy.Cursor(api.home_timeline).items(10):
        # Process a single status
        dictt = status._json
        print(dictt['user']['name'])
        print(dictt['text'])
        print(dictt['created_at'])
