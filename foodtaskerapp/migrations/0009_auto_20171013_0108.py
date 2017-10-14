# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-13 01:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0008_auto_20171012_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Driver'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(2, 'Ready'), (3, 'On the way'), (4, 'Delivered'), (1, 'Cooking')]),
        ),
    ]
