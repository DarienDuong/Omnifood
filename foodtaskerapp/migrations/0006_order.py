# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-12 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0005_auto_20171010_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('total', models.FloatField()),
                ('status', models.IntegerField(choices=[(4, 'Delivered'), (3, 'On the way'), (2, 'Ready'), (1, 'Cooking')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('picked_at', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Customer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Driver')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Restaurant')),
            ],
        ),
    ]
