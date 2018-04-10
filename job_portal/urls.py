
from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/',views.contract,name = 'contract'),
    path('faq',views.faq,name = 'faq'),
    path('about',views.about,name='about')
]