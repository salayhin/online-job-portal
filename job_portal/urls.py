
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/',views.contact,name = 'contact'),
    path('faq',views.faq,name = 'faq'),
    path('about',views.about,name='about'),
    path('companies/<id>/', views.companies, name='companies'),
    path('company_jobs/<id>/', views.company_jobs, name='company_jobs'),
]