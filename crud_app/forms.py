from django import forms

from crud_app.models import Company, Job
from django.forms import Textarea


class CompanyForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'autocomplete':'off'}))
    age = forms.IntegerField(required=True)
    employee_count = forms.IntegerField(required=True)
    dev_count = forms.IntegerField(required=True)
    spolsky_1 = forms.BooleanField(required=False)
    spolsky_2 = forms.BooleanField(required=False)
    spolsky_3 = forms.BooleanField(required=False)
    spolsky_4 = forms.BooleanField(required=False)
    spolsky_5 = forms.BooleanField(required=False)
    spolsky_6 = forms.BooleanField(required=False)
    spolsky_7 = forms.BooleanField(required=False)
    spolsky_8 = forms.BooleanField(required=False)
    spolsky_9 = forms.BooleanField(required=False)
    spolsky_10 = forms.BooleanField(required=False)
    spolsky_11 = forms.BooleanField(required=False)
    spolsky_12 = forms.BooleanField(required=False)
    projectoriented = forms.BooleanField(required=False)
    logo = forms.FileField(required=False)

    class Meta:

        model = Company
        exclude = []

class JobForm(forms.ModelForm):
    job_title = forms.CharField(required=False)
    salary_range_from = forms.IntegerField(required=False)
    salary_range_to = forms.IntegerField(required=False)
    techstack = forms.CharField(required=False)
    location = forms.CharField(required=False)
    remotework = forms.BooleanField(required=False)
    parttime = forms.BooleanField(required=False)
    backend = forms.IntegerField(required=False)
    frontend = forms.IntegerField(required=False)
    job_desc = forms.CharField(required=False, widget=Textarea)
    start_date = forms.DateField(required=False)
    expiry = forms.DateField(required=False)

    class Meta:

        model = Job
        exclude = []

