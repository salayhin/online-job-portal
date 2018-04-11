# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Faq, BusinessType, Job, Contract
from .forms import contract_form
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
        form = contract_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            form.save()
    return render(request, 'contact.html',{'form':contract_form})


def faq(request):
    faq = Faq.objects.all()
    return render(request, 'faq.html',{'faq':faq})


def about(request):
    return render(request,'about.html')

