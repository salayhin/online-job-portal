# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import BusinessType
<<<<<<< HEAD
from .models import Company, Contract
=======
from .models import Company
from .models import Job
>>>>>>> 7328875c32bf7d7f6f9ac051d07ae1110e545384

from django.contrib import admin

# Register your models here.

admin.site.register(BusinessType)
admin.site.register(Company)
<<<<<<< HEAD
admin.site.register(Contract)
=======
admin.site.register(Job)
>>>>>>> 7328875c32bf7d7f6f9ac051d07ae1110e545384
