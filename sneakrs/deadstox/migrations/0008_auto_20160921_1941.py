# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deadstox', '0007_auto_20160921_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneakers',
            name='closet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sneakers', to='deadstox.Closets'),
            preserve_default=False,
        ),
    ]
