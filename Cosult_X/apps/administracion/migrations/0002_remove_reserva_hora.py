# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-12-12 21:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='hora',
        ),
    ]
