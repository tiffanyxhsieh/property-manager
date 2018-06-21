from django.db import models
from housing_application.models import HousingApplication
from accounts.models import Customer
# Create your models here.


class Property(models.Model):
    address = models.CharField(max_length=250)
    housing_application = models.ForeignKey(HousingApplication, on_delete=models.PROTECT)
    occupied_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    publicly_available = models.BooleanField(default=False)
