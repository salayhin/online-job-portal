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
