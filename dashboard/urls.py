from django.urls import path, include
from django.views.generic.base import TemplateView


app_name='Dashboard'
urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),

]