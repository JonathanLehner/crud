# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 15:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cf_app', '0009_job_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_title',
            new_name='title',
        ),
    ]
