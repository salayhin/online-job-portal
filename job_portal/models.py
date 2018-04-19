# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
#from django.utils import timezone
from django.contrib.auth.models import User

class BusinessType(models.Model):
    type = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type


class Company(models.Model):
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    business = models.TextField()
    office_address = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    total_employee = models.IntegerField()
    year_established = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.name


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    total_vacancy = models.IntegerField()
    job_nature = models.CharField(max_length=100)
    educational_requirement = models.TextField()
    job_requirement = models.TextField()
    job_location = models.TextField()
    company_benefit = models.TextField()
    year_of_experience = models.CharField(max_length=50)
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


class Faq(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name=models.CharField(max_length=200)
    fathers_name=models.CharField(max_length=150)
    mothers_name=models.CharField(max_length=150)
    date_of_birth = models.DateField()
    present_address=models.TextField()
    permanent_address=models.TextField()
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    phone=models.CharField(max_length=25)
    email=models.EmailField()
    nationality=models.CharField(max_length=120)
    national_id=models.IntegerField()
    skills=models.TextField()
    religion=models.CharField(max_length=20)
    sex=models.CharField(max_length=10)
    marital_status=models.CharField(max_length=15)
    hobby=models.CharField(max_length=250, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EmployeeEducation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    exam = models.CharField(max_length=200)
    session = models.CharField(max_length=50)
    passing_year = models.CharField(max_length=50)
    result = models.CharField(max_length=120)
    board = models.CharField(max_length=120)
    university = models.CharField(max_length=120)
    subject = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class EmployeeExperience(models.Model):
    emp_education = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_title=models.CharField(max_length=250)
    company_name=models.CharField(max_length=250)
    start_date=models.DateField()
    end_date=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_title

class EmployeeJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    expected_salary = models.IntegerField()
    cover_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



