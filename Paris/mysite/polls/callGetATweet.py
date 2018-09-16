#!/usr/bin/env python3
from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
from . import getATweet as gt
import datetime
from . import saveATweet as sv
cnx = mysql.connector.connect(user='szhao4',password='A1239877a', database='haha')
from .models import Tweet
from django.utils.encoding import smart_text
from smartencoding import smart_unicode
import re
import random
re_pattern = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
def filter_using_re(unicode_string):
    return re_pattern.sub(u'\uFFFD', unicode_string)



listt = []
data_tweet = ()
sv.getData(listt)

add_tweet = ("INSERT INTO tweets2 "
               "(text, user, time) "
               "VALUES (%s, %s, %s)")

cursor = cnx.cursor()
cursor.execute('SET NAMES utf8mb4')
cursor.execute("SET CHARACTER SET utf8mb4")
cursor.execute("SET character_set_connection=utf8mb4")
a = Tweet.objects.all()
print((a[1].text))
#print(Tweet.objects.all())
def callbackMethod(tweet):
    seconds = float(tweet.timestamp_ms) / 1000.0
    b = Tweet(user = filter_using_re(tweet.user.name), text= filter_using_re(tweet.text), time= filter_using_re(datetime.datetime.fromtimestamp(seconds).strftime('%Y-%m-%d %H:%M:%S.%f')), cluster=random.randint(1,7), post_id = tweet.id)
    b.save()

def call(ok):
    for i in range(10):
        gt.getATweet(callbackMethod, ok)
        
    #    cursor.execute(add_tweet, data_tweet)
    #    cnx.commit()
       


# Insert salary information

# Make sure data is committed to the database

    cursor.close()
    cnx.close()
