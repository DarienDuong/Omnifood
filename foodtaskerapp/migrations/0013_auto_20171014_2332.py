# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-14 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0012_auto_20171014_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(4, 'Delivered'), (3, 'On the way'), (2, 'Ready'), (1, 'Cooking')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(),
        ),
    ]
