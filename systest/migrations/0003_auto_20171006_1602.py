# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-06 15:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('systest', '0002_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ModuleName', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('system_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systest.System')),
            ],
        ),
        migrations.CreateModel(
            name='TestOverview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('ExpectedOutcome', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systest.Module')),
            ],
        ),
        migrations.AddField(
            model_name='version',
            name='created_by',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='version',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
