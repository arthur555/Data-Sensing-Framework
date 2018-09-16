#!/usr/bin/env python3
import requests
import os
from IPython.display import HTML
from ipywidgets import interact
from datetime import date, datetime, timedelta
import mysql.connector
import datetime
cnx = mysql.connector.connect(user='szhao4',password='A1239877a', database='haha')
from .models import Tweet
from django.utils.encoding import smart_text
import re


# Functions
ORDERBY = {
    'Score': 'score',
    'Creation Time': 'created_utc',
    'Title': 'title'
}

from .models import Tweet
def multireddit(subreddits, limit=5, orderby='score'):
    obj = Tweet.objects.all()  
    print(obj[1])
    #words = subreddits.split(',')
   
    #articles=[]
    #for word in words:
    #    headers  = {'user-agent': 'reddit-{}'.format(os.environ['USER'])}
    #    response = requests.get('https://www.reddit.com/r/{}/.json'.format(word), headers=headers)
    
    #    if not response:
    #        return
    
    
    
     #   data=(response.json()['data']['children'])
     #   for dat in data:
     #       articles.append(dat['data']) 


   
    #html='<table><tbody>'
    #for index, article in enumerate(sorted(articles, key=lambda a: a[orderby])[:-limit-1:-1]):
    #    html += '''
    #    <tr>
    #        <td>{}</td>
    #        <td style="text-align: left"><a href="{}" target="_blank">{}</a></td>
    #        <td style="text-align: left"><i>{}</i></td>
    #        <td style="text-align: left"><a href="https://www.reddit.com/{}" target="_blank">Comments</a></td>
    #    </tr>
    #    '''.format(index + 1, article['url'], article['title'], article['score'],article['permalink'])
        
        
    #html += '</tbody></table>'

if __name__ == '__main__':
    multireddit ("haha")


    #display(HTML(html))
    
   # interact(multireddit, subreddits='', limit=(1, 20), orderby=ORDERBY)
