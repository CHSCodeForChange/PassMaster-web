# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-26 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_pass_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='pass',
            name='requester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pass_requester', to='server.Student'),
        ),
    ]
