# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-11-20 21:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cf_app', '0004_auto_20161120_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='noemail', max_length=254)),
                ('job_title', models.TextField(default='nojobtitle')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cf_app.Company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
