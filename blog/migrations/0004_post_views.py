# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180604_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0, verbose_name='阅读次数'),
        ),
    ]
