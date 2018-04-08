
from django.urls import path, include
from . import views

urlpatterns = [
    path('contract/',views.contract,name = 'contract'),
    path('faq',views.faq,name = 'faq'),
    path('about',views.about,name='about')
]