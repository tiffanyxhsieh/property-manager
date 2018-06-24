from django.db import models
from accounts.models import Customer
from localflavor.us.models import USZipCodeField, USStateField
# Create your models here.

#TODO: have a way to see property history (previous tenants)


class Property(models.Model):
    unit = models.CharField(max_length=10, default='')
    street_address = models.CharField(max_length=100, default='0')
    state = USStateField(default='')
    zip_code = USZipCodeField(default='')
    occupied_by = models.OneToOneField(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    publicly_available = models.BooleanField(default=False)

    def __str__(self):
        address = self.street_address
