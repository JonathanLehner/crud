# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 15:35
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='noname')),
                ('email', models.EmailField(default='noemail', max_length=254)),
                ('streak_emails', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(default='noemail', max_length=254), default=[], size=None)),
                ('notes', models.TextField(default='noname')),
                ('job_title', models.TextField(default='nojobtitle')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('notes', models.TextField(default='nonotes')),
                ('name', models.TextField(default='noname', unique=True)),
                ('career_page_url', models.URLField(default='http://none.com')),
                ('employee_count', models.IntegerField(default=0)),
                ('dev_count', models.IntegerField(default=0)),
                ('spolsky_1', models.BooleanField(default=False)),
                ('spolsky_2', models.BooleanField(default=False)),
                ('spolsky_3', models.BooleanField(default=False)),
                ('spolsky_4', models.BooleanField(default=False)),
                ('spolsky_5', models.BooleanField(default=False)),
                ('spolsky_6', models.BooleanField(default=False)),
                ('spolsky_7', models.BooleanField(default=False)),
                ('spolsky_8', models.BooleanField(default=False)),
                ('spolsky_9', models.BooleanField(default=False)),
                ('spolsky_10', models.BooleanField(default=False)),
                ('spolsky_11', models.BooleanField(default=False)),
                ('spolsky_12', models.BooleanField(default=False)),
                ('projectoriented', models.BooleanField(default=False)),
                ('logo', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.TextField(default='nojobtitle')),
                ('link', models.URLField(default='http://none.com')),
                ('salary_range_from', models.IntegerField(default=0)),
                ('salary_range_to', models.IntegerField(default=0)),
                ('techstack', models.TextField(default='notechstack')),
                ('location', models.TextField(default='nolocation')),
                ('remotework', models.BooleanField(default=False)),
                ('parttime', models.BooleanField(default=False)),
                ('backend', models.IntegerField(default=0)),
                ('frontend', models.IntegerField(default=0)),
                ('job_desc', models.TextField(default='nodesc')),
                ('start_date', models.DateField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))),
                ('expiration_date', models.DateField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))),
                ('active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_app.Company')),
            ],
        ),
        migrations.CreateModel(
            name='OtherPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='noquestion')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_app.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='noemail', max_length=254)),
                ('job_title', models.TextField(default='nojobtitle')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_app.Company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bookmark',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_app.Job'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
