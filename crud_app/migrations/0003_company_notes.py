# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-11-20 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cf_app', '0002_homepage_otherpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='notes',
            field=models.TextField(default='nonotes'),
        ),
    ]
