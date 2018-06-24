from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

app_name='Dashboard'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),

]