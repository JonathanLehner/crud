import os
import simplejson
import requests
from requests.auth import HTTPBasicAuth

from django.contrib.auth.models import User

from django.utils import timezone

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import filters
from rest_framework import generics

from .models import Company, CandidateProfile
from .models import Job

from .forms import CompanyForm, JobForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from rest_framework import viewsets
from .serializers import CompanySerializer, UserSerializer, JobSerializer, CandidateSerializer
from django.shortcuts import get_object_or_404


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CompanyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        job_form = JobForm()
        company_form = CompanyForm()

    return render(request, 'crud_app/company_reg.html', {'job_form': job_form, 'company_form': company_form})


def match(request, keyword):
    c = Company.objects.filter(notes__icontains=keyword)
    ca = CandidateProfile.objects.filter(notes__icontains=keyword)

    return render(request, 'crud_app/match.html', {'companies': c, "candidates": ca})


def index2(request, message):

    return render(request, 'crud_app/base.html', {'message': message})


def about(request):

    return render(request, 'crud_app/base.html')


class CompanyView(DetailView):

    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class JobView(DetailView):

    model = Job

    def get_context_data(self, **kwargs):
        context = super(JobView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CompanyAdmin(DetailView):

    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyAdmin, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class Profile(DetailView):

    model = User

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class JobList(ListView):

    model = Job

    def get_context_data(self, **kwargs):
        context = super(JobList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        form = JobForm()
        context['form'] = form
        return context


class CompanyList(ListView):

    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CompanySearchList(ListView):

    template_name = 'crud_app/company_list.html'

    def get_queryset(self):
        c = Company.objects.filter(name__contains=self.args[0])
        for i in range(20):
            print(c)
        return c

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CompanySearchList, self).get_context_data(**kwargs)
        return context


class CompanyListApi(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('notes', 'name')


class JobListApi(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('job_title', 'company__name', 'techstack')


class CandidateListApi(generics.ListAPIView):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','notes')


class CandidateList(ListView):

    template_name = 'crud_app/candidate_list.html'

    model = CandidateProfile

    def get_context_data(self, **kwargs):
        context = super(CandidateList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CandidateSearchList(ListView):

    template_name = 'crud_app/candidate_list.html'

    def get_queryset(self):
        c = CandidateProfile.objects.filter(name__contains=self.args[0])

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CandidateSearchList, self).get_context_data(**kwargs)
        return context


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Job.objects.all().order_by('-start_date')
    serializer_class = JobSerializer


def get_streak_companies(request):
    import requests
    from requests.auth import HTTPBasicAuth
    import simplejson
    f = requests.get(
        "https://www.streak.com/api/v1/pipelines/agxzfm1haWxmb29nYWVyMQsSDE9yZ2FuaXphdGlvbiIKZ3VsZW5rby5jaAwLEghXb3JrZmxvdxiAgICA4MGcCgw/boxes",
        auth=HTTPBasicAuth(os.environ.get('STREAK_KEY'), ''))
    data = simplejson.loads(f.text)
    res = []
    i = 0
    for item in data:
        if item.get("stageKey") == "5008":
            i += 1
            res.append(item)
            obj, created = Company.objects.update_or_create(name=item['name'], defaults={'notes': item.get('notes', 'nonotes')})
    print(i)
    return HttpResponseRedirect('/companies/')


def get_jobs_from_web(request):
    # still mocked
    jobs = [{'title': 'Frontend genuis', 'link': 'https://www.ti8m.ch/en/career/internalJobDetail?uuid=bf452182-1c8a-4de0-b14b-2a6be9d928c2'},
            {'title': 'C# Ninja', 'link': 'https://www.ti8m.ch/en/career/internalJobDetail?uuid=04534b58-3363-4c3f-988d-610b5e81d805'}]
    for item in jobs:
        j = Job(job_title=item['title'], link=item['link'], company=Company.objects.filter(name='Ti8m').first())
        j.save()
    return HttpResponseRedirect('/jobs/')


def get_streak_candidates(request):
    f = requests.get(
        "https://www.streak.com/api/v1/pipelines/agxzfm1haWxmb29nYWVyMQsSDE9yZ2FuaXphdGlvbiIKZ3VsZW5rby5jaAwLEghXb3JrZmxvdxiAgICAoI6BCgw/boxes",
        auth=HTTPBasicAuth(os.environ.get('STREAK_KEY'), ''))

    data = simplejson.loads(f.text)
    res = []
    i = 0
    for item in data:
        i += 1
        res.append(item)

        if 'iwan@gulenko.ch' in item['emailAddressesAutoExtracted']: item['emailAddressesAutoExtracted'].remove('iwan@gulenko.ch')
        mails = item.get("emailAddressesAutoExtracted", "no mails")

        obj, created = CandidateProfile.objects.update_or_create(name=item['name'],
                                                                 defaults={'notes': item.get('notes', 'nonotes'),
                                                                           'streak_emails': item.get('emailAddressesAutoExtracted', [])})

    return HttpResponseRedirect('/candidates/')
