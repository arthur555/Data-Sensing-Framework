#!/usr/bin/env python3
from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
from . import getATweet as gt
import datetime
from . import saveATweet as sv
#cnx = mysql.connector.connect(user='szhao4',password='A1239877a', database='haha')
from .models import Tweett
from django.utils.encoding import smart_text
from smartencoding import smart_unicode
listt = []
data_tweet = ()
sv.getData(listt)

#add_tweet = ("INSERT INTO tweets2 "
#               "(text, user, time) "
#               "VALUES (%s, %s, %s)")

#cursor = cnx.cursor()

def callbackMethod(tweet):
#    global listt
#    global data_tweet
#    listt[0] = tweet.text
#    listt[1] = tweet.user.name
    seconds = float(tweet.timestamp_ms) / 1000.0
#    listt[2] = datetime.datetime.fromtimestamp(seconds).strftime('%Y-%m-%d %H:%M:%S.%f')
#    data_tweet = (listt[0], listt[1], listt[2])
    b = Tweett(user = smart_text(tweet.user.name, encoding = 'utf-8', strings_only= False, errors='strict'), text= smart_text(tweet.text, encoding = 'utf-8', strings_only = False, errors = 'strict'), time= smart_text(datetime.datetime.fromtimestamp(seconds).strftime('%Y-%m-%d %H:%M:%S.%f'), encoding = 'utf-8', strings_only=False, errors= 'strict'))
    b.save()

def call(ok):
    for i in range(10):
        gt.getATweet(callbackMethod, ok)
        
    #    cursor.execute(add_tweet, data_tweet)
    #    cnx.commit()
       


# Insert salary information

# Make sure data is committed to the database

 #   cursor.close()
 #   cnx.close()
