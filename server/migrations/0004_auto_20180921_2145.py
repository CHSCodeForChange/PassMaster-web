# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-22 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_location_specialsrtpass'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialsrtpass',
            name='session',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='specialsrtpass',
            name='timeArrivedOrigin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='specialsrtpass',
            name='timeLeftDestination',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
