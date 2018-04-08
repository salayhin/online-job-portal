# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Contract
from .forms import contract_form
from .models import FAQ
import pdb

# Create your views here.

def contract(request):
    if request.method == 'POST':

        form = contract_form(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'job_portal/contract.html',{'form':contract_form})



# Create your views here.

def faq(request):
    all = FAQ.objects.all()
    return render(request, 'faq.html',{'faq':all})


def about(request):
    return render(request,'about.html')

