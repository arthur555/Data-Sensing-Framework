#!/usr/bin/env python3
import getATweet as gt
import datetime

def callbackMethod(tweet):
    print('text: {}'.format(tweet.text))
    print('user: {}'.format(tweet.user.name))
    seconds = float(tweet.timestamp_ms) / 1000.0
    date = datetime.datetime.fromtimestamp(seconds).strftime('%Y-%m-%d %H:%M:%S.%f')
    print('timestamp: {}'.format(date))
gt.getATweet(callbackMethod, "hello", 10)
