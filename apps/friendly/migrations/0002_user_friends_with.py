# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-01 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendly', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends_with',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_friends_with_+', to='friendly.User'),
        ),
    ]
