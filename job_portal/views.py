# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Faq, BusinessType, Job, Contract
from .forms import ContractForm,EmployeeForm,EmployeeEducationForm,EmployeeExperinenceForm,EmployeeJobForm
import pdb


def home(request):
    business_types = BusinessType.objects.all()
    return render(request, 'home.html', {'business_types': business_types})


def companies(request, id):

    business_type = BusinessType.objects.get(id=id)
    companies = business_type.company_set.all()

    return render(request, 'companies.html', {'companies': companies})


def company_jobs(request, id):
    company_jobs = Job.objects.filter(company_id=id)

    return render(request, 'company_jobs.html', {'company_jobs': company_jobs})


def contact(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            form.save()
    return render(request, 'contact.html',{'form':ContractForm})


def faq(request):
    faq = Faq.objects.all()
    return render(request, 'faq.html',{'faq':faq})


def about(request):
    return render(request,'about.html')

def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            fathers_name = form.cleaned_data['fathers_name']
            mothers_name = form.cleaned_data['mothers_name']
            present_address = form.cleaned_data['present_address']
            form.save()

    else:
        form = EmployeeForm()

    return render(request, 'employee.html',{'form':EmployeeForm})


def employee_education(request):
    if request.method == 'POST':
        form = EmployeeEducationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = EmployeeEducationForm()

    return render(request, 'employee_education.html',{'form':EmployeeEducationForm})


def employee_experience(request):
    if request.method == 'POST':
        form = EmployeeExperinenceForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = EmployeeExperinenceForm()

    return render(request, 'employee_experience.html',{'form':EmployeeExperinenceForm})

def employee_job(request):
    if request.method == 'POST':
        form = EmployeeJobForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = EmployeeJobForm()

    return render(request, 'employee_job.html',{'form':EmployeeJobForm})