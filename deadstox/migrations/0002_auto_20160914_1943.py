# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deadstox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneakers',
            name='images',
            field=models.FilePathField(null=True),
        ),
    ]