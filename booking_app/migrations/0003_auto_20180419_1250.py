# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-19 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_auto_20180418_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(),
        ),
    ]
