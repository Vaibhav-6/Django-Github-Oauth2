from django.contrib import admin
from django.urls import path,include
from login import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',views.index,name='home1'),
    path('trending/',views.trending,name='home2'),
    # path('trending/',views.trending,name='home2')
]
