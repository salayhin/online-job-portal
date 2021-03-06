
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/',views.contact,name = 'contact'),
    path('faq',views.faq,name = 'faq'),
    path('about',views.about,name='about'),
    path('employee/',views.employee,name='employee'),
    path('employee_experience/',views.employee_experience,name='employee_experience'),
    path('employee_education/',views.employee_education,name='employee_education'),
    path('apply/',views.employee_job,name='employee_job'),
    path('companies/<id>/', views.companies, name='companies'),
    path('company_jobs/<id>/', views.company_jobs, name='company_jobs'),
    path('signup/', views.signup, name='signup'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]