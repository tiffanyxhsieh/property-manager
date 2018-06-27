from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PropertyListAll.as_view(), name='property_list'),
    path('<uuid:pk>/', views.PropertyDetailView.as_view(), name='property_detail'),
]
