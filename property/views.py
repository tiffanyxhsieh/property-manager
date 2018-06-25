from django.shortcuts import render
from property.models import Property
from django.views import generic
# Create your views here.


class PropertyListAll(generic.ListView):
    model = Property
    paginate_by = 30


class PropertyDetailView(generic.DetailView):
    model = Property
