from django.db import models
import datetime
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User

#class Post(models.Model):
#    post = models.CharField(max_length=500)
#    user = models.ForeignKey(User,on_delete=models.CASCADE)

#class KeyForm(forms.Form):
#    key = forms.CharField(label='Your key', max_length=100)

#class Question(models.Model):
 #   question_text = models.CharField(max_length=200)
 #   pub_date = models.DateTimeField('date published')
 #   def __str__(self):
 #       return self.question_text
 #   def was_published_recently(self):
 #       return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#class Choice (models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length =200)
#    votes = models.IntegerField(default=0)
#    def __str__(self):
#        return self.choice_text
# Create your models here.

class Tweett(models.Model):
    user = models.CharField(max_length = 200)
    text = models.CharField(max_length = 200)
    time = models.CharField(max_length = 100)
    cluster = models.IntegerField(default = 0)
    def __str__(self):
        return self.user
