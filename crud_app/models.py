from __future__ import unicode_literals

from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from django.db import models
import datetime
#
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

# Create your models here.

class Company(models.Model):
    age = models.IntegerField(default=0)
    notes = models.TextField(default="nonotes")
    name = models.TextField(default="noname", unique=True)
    career_page_url = models.URLField(default="http://none.com")
    employee_count = models.IntegerField(default=0)
    dev_count = models.IntegerField(default=0)
    spolsky_1 = models.BooleanField(default=False)
    spolsky_2 = models.BooleanField(default=False)
    spolsky_3 = models.BooleanField(default=False)
    spolsky_4 = models.BooleanField(default=False)
    spolsky_5 = models.BooleanField(default=False)
    spolsky_6 = models.BooleanField(default=False)
    spolsky_7 = models.BooleanField(default=False)
    spolsky_8 = models.BooleanField(default=False)
    spolsky_9 = models.BooleanField(default=False)
    spolsky_10 = models.BooleanField(default=False)
    spolsky_11 = models.BooleanField(default=False)
    spolsky_12 = models.BooleanField(default=False)
    projectoriented = models.BooleanField(default=False)
    logo = models.FileField(blank=True)

    def __str__(self):
        return '%s %s' % (self.name, self.career_page_url if self.career_page_url != "http://none.com" else "")


class Job(models.Model):
    company = models.ForeignKey(Company)
    job_title = models.TextField(default="nojobtitle")
    link = models.URLField(default="http://none.com")
    salary_range_from = models.IntegerField(default=0)
    salary_range_to = models.IntegerField(default=0)
    techstack = models.TextField(default="notechstack")
    location = models.TextField(default="nolocation")
    remotework = models.BooleanField(default=False)
    parttime = models.BooleanField(default=False)
    backend = models.IntegerField(default=0)
    frontend = models.IntegerField(default=0)
    job_desc = models.TextField(default="nodesc")
    start_date = models.DateField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))
    expiration_date = models.DateField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s' % (self.company, self.job_title)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(default='noemail')
    job_title = models.TextField(default='nojobtitle')
    company = models.ForeignKey(Company)

    def __str__(self):
        return '%s - %s' % (self.user, self.job_title)

class CandidateProfile(models.Model):
    name = models.TextField(default='noname')
    email = models.EmailField(default='noemail')
    streak_emails = ArrayField(
        models.EmailField(default='noemail'), default=[])
    notes = models.TextField(default='noname')
    job_title = models.TextField(default='nojobtitle')

    def __str__(self):
        return '%s - %s' % (self.user, self.job_title)

class Bookmark(models.Model):
    user = models.ForeignKey(User)
    job = models.ForeignKey(Job)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.user, self.job)

class Question(models.Model):
    user = models.ForeignKey(User)
    job = models.ForeignKey(Job)
    text = models.TextField(default='noquestion')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.user, self.text)


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full')
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)

        # Add extra variables and return the updated context
        context['time'] = timezone.now()
        return context

class OtherPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full')
    ]

    def get_context(self, request):
        context = super(OtherPage, self).get_context(request)

        # Add extra variables and return the updated context
        context['time'] = timezone.now()
        return context

