# Generated by Django 2.1.dev20180216185855 on 2018-02-25 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweett',
            fields=[
                ('user', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=100)),
                ('cluster', models.IntegerField(default = 0)),
            ],
        ),
    ]