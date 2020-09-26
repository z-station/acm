# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-20 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_auto_20200412_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='content',
            field=models.TextField(blank=True, default='', verbose_name='листинг решения'),
        ),
        migrations.AddField(
            model_name='solution',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата/время отправки'),
        ),
        migrations.AddField(
            model_name='solution',
            name='is_locked',
            field=models.BooleanField(default=False, verbose_name='запрещено изменять'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='is_count',
            field=models.BooleanField(default=True, verbose_name='баллы идут в зачет'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='taskitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='training.TaskItem', verbose_name='задача'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата/время окончения решения задач в формате UTC'),
        ),
    ]
