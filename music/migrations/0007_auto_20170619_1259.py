# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-19 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20170619_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music_info_detail',
            old_name='played_times',
            new_name='music_played_times',
        ),
        migrations.RenameField(
            model_name='music_info_detail',
            old_name='popularity',
            new_name='music_popularity',
        ),
    ]
