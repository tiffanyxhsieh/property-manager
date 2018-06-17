from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerForm, UserForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import propertymanager
from .models import Customer
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator

from django.forms.formsets import formset_factory

#TODO: check for unique email
#TODO: figure out how to redirect after sign up submission

def customer_signup(request):
    if request.method == 'POST':
        basic_user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if basic_user_form.is_valid() and customer_form.is_valid() :
            user = User.objects.create_user(username=basic_user_form.cleaned_data['username'],
                                            password=basic_user_form.cleaned_data['password'])
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            HttpResponseRedirect(reverse_lazy(':home'))


    else:
        basic_user_form = UserForm()
        customer_form = CustomerForm()

    return render(request, 'signup.html', {'basic_user_form': basic_user_form,
                                           'customer_form': customer_form})
