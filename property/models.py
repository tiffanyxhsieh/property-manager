import uuid
from django.db import models
from django.urls import reverse
from accounts.models import Customer
from localflavor.us.models import USZipCodeField, USStateField

#TODO: have a way to see property history (previous tenants)...make occupied_by an array?


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    unit = models.CharField(max_length=10, default='')
    street_address = models.CharField(max_length=100, default='0')
    state = USStateField(default='')
    zip_code = USZipCodeField(default='')
    occupied_by = models.OneToOneField(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    publicly_available = models.BooleanField(default=False)
    num_bedrooms = models.IntegerField(default=1)
    num_bathrooms = models.IntegerField(default=1)

    def __str__(self):
        address = self.unit + ' ' + self.street_address
        return address

    #def get_absolute_url(self):
    #    return reverse('property-detail', args=[str(self.id)])



