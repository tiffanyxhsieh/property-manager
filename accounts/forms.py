from .models import Customer
from django.forms import ModelForm
from django.contrib.auth.models import User


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['phone_number','date_of_birth']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'password', 'email']