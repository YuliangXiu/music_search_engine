# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-19 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170412_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music_info_detail',
            name='album_cover_path',
        ),
        migrations.RemoveField(
            model_name='music_info_detail',
            name='lyric_path',
        ),
        migrations.RemoveField(
            model_name='music_info_detail',
            name='music_path',
        ),
        migrations.RemoveField(
            model_name='music_info_detail',
            name='music_type_label',
        ),
        migrations.AddField(
            model_name='music_info_detail',
            name='music_album_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='music_info_detail',
            name='music_lyric_content',
            field=models.CharField(blank=True, default=' ', max_length=5000),
        ),
        migrations.AddField(
            model_name='music_info_detail',
            name='music_singer_id',
            field=models.IntegerField(default=0),
        ),
    ]