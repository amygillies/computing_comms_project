# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computingcomms', '0003_auto_20180315_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
