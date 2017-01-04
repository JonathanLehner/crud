from django.views.generic import TemplateView
from . import views

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers
from .views import CompanyView, JobList, CompanyList, CompanySearchList, CandidateList, CandidateSearchList, JobView, CompanyAdmin, Profile, \
    CompanyListApi, JobListApi, CandidateListApi

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'jobs', views.JobViewSet)

urlpatterns = [
    url(r'^$', views.about, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^pages/', include(wagtail_urls)),

    url(r'^company/(?P<pk>[0-9]+)/$', CompanyView.as_view(), name='company-detail'),
    url(r'^job/(?P<pk>[0-9]+)/$', JobView.as_view(), name='cf-job-detail'),
    url(r'^jobs/$', JobList.as_view(), name='cf-job-list'),
    url(r'^jobs_api/$', staff_member_required(JobListApi.as_view()), name='job-list-api'),
    url(r'^company_admin/(?P<pk>[0-9]+)/$', CompanyAdmin.as_view(), name='company-admin'),
    url(r'^companies/$', staff_member_required(CompanyList.as_view()), name='companies'),
    url(r'^companies/([\w-]+)/$', staff_member_required(CompanySearchList.as_view()), name='company-search-list'),
    url(r'^companies_api/$', staff_member_required(CompanyListApi.as_view()), name='company-list-api'),
    url(r'^candidates/$', staff_member_required(CandidateList.as_view()), name='candidates'),
    url(r'^candidates/([\w-]+)/$', staff_member_required(CandidateSearchList.as_view()), name='candidate-search-list'),
    url(r'^candidates_api/$', staff_member_required(CandidateListApi.as_view()), name='candidate-list-api'),
    url(r'^match/(?P<keyword>[\w-]+)/$', views.match, name='match-list'),
    url(r'^profile/(?P<pk>[0-9]+)/$', login_required(Profile.as_view()), name='profile'),

    url(r'^company_registration/$', login_required(views.index), name='company_registration'),
    url(r'^get_jobs_from_web', staff_member_required(views.get_jobs_from_web), name='get_jobs_from_web'),
    url(r'^company_registration_info/$', TemplateView.as_view(template_name='cf_app/company_reg_info.html'), name='company_reg_info'),  #TemplateView.as_view(template_name='company_reg_info.html'
    url(r'^msg/(?P<message>[\w{}.-]{1,40})/$', views.index2, name='index2'),

    url(r'^api/', include(router.urls)),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    # url(r'', include(wagtail_urls)),   we don't need this

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








### only for dev, in prod configure apache for it

