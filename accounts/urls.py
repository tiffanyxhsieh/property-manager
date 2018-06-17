from django.urls import path

from . import views
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.shortcuts import redirect


urlpatterns = [
    path('signup/', views.customer_signup, name='signup'),

]
