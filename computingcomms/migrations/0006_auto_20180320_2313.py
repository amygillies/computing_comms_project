# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computingcomms', '0005_auto_20180320_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]