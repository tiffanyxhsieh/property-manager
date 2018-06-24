from django.db import models
from housing_application.models import HousingApplication
from accounts.models import Customer
from localflavor.us.models import USZipCodeField, USStateField
# Create your models here.


class Property(models.Model):
    street_address = models.CharField(max_length=100, default='0')
    state = USStateField
    zip_code = USZipCodeField
    housing_application = models.ForeignKey(HousingApplication, on_delete=models.PROTECT)
    occupied_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    publicly_available = models.BooleanField(default=False)
