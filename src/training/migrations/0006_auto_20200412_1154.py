# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-12 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20200406_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='is_count',
            field=models.BooleanField(default=True, help_text='решение идет вне зачета если, например, просрочено', verbose_name='баллы идут в зачет'),
        ),
        migrations.AddField(
            model_name='topic',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата окончения решения задач'),
        ),
    ]
