# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-30 23:54
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('startTimeRequested', models.TimeField(blank=True, null=True)),
                ('endTimeRequested', models.TimeField(blank=True, null=True)),
                ('timeLeftOrigin', models.TimeField(blank=True, null=True)),
                ('timeArrivedDestination', models.TimeField(blank=True, null=True)),
                ('description', models.CharField(max_length=960, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idName', models.CharField(default='stuff', max_length=250)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='LocationPass',
            fields=[
                ('pass_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='passes.Pass')),
                ('location', models.CharField(blank=True, max_length=12, null=True)),
            ],
            bases=('Passes.pass',),
        ),
        migrations.CreateModel(
            name='SRTPass',
            fields=[
                ('pass_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='passes.Pass')),
                ('session', models.CharField(blank=True, max_length=1, null=True)),
                ('timeLeftDestination', models.TimeField(blank=True, null=True)),
                ('timeArrivedOrigin', models.TimeField(blank=True, null=True)),
                ('destinationTeacher',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   related_name='destinationTeacherSRT', to='passes.Teacher')),
            ],
            bases=('Passes.pass',),
        ),
        migrations.CreateModel(
            name='TeacherPass',
            fields=[
                ('pass_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='passes.Pass')),
                ('destinationTeacher',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   related_name='destinationTeacher', to='passes.Teacher')),
            ],
            bases=('Passes.pass',),
        ),
        migrations.AddField(
            model_name='student',
            name='defaultOrgin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='srt_teacher', to='passes.Teacher'),
        ),
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='teacher_list', to='passes.Teacher'),
        ),
        migrations.AddField(
            model_name='pass',
            name='originTeacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pass_origin_teacher',
                                    to='passes.Teacher'),
        ),
        migrations.AddField(
            model_name='pass',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pass_student',
                                    to='passes.Student'),
        ),
    ]