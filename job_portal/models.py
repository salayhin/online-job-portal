# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class BusinessType(models.Model):
    type = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type

class Company(models.Model):
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    business = models.TextField()
    office_address = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    total_employee = models.IntegerField()
    year_established = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    total_vacancy = models.IntegerField()
    job_nature = models.CharField(max_length=150)
    educational_requirement = models.TextField()
    job_requirement = models.TextField()
    job_location = models.TextField()
    company_benefit = models.TextField()
    year_of_experience = models.TextField()
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    skill_sets = models.TextField()
    published_date = models.DateTimeField()
    deadline = models.DateField()
    is_published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
