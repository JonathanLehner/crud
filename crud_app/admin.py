from django.contrib import admin

# Register your models here.

from .models import Job, CandidateProfile, Company

admin.site.register(Job)
admin.site.register(Company)
admin.site.register(CandidateProfile)
