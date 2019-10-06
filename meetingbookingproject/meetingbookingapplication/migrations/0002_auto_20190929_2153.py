# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-29 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meetingbookingapplication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='mdescription',
            new_name='meetingdescription',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='mid',
            new_name='meetingid',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='mroom',
            new_name='meetingroom',
        ),
        migrations.AddField(
            model_name='staff',
            name='staffmail',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='staffname',
            field=models.CharField(max_length=50),
        ),
    ]