# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systest', '0009_auto_20171009_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='install_live_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
