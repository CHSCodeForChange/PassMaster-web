# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-05 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Passes', '0002_auto_20180705_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pass',
            name='location',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='pass',
            name='timeArrivedDestination',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pass',
            name='timeLeftOrigin',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
