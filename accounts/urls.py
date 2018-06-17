from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.customer_signup, name='signup'),
]
