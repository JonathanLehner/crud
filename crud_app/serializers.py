from django.contrib.auth.models import User
from .models import Company, Job, CandidateProfile
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'notes')


class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name', read_only=True)  ###replaces the other company

    class Meta:
        model = Job
        fields = ('company', 'company_name', 'job_title', 'job_desc', 'salary_range_from', 'salary_range_to')


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = ('name', 'streak_emails', 'notes')