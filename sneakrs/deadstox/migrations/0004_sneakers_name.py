# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deadstox', '0003_auto_20160914_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneakers',
            name='name',
            field=models.CharField(max_length=48, null=True),
        ),
    ]