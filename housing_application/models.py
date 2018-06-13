from django.db import models
from customer_account.models import Customer
from property.models import Property
# Create your models here.


class HousingApplication(models.Model):
    date_application_submitted = models.DateTimeField()
    applicants = models.ManyToManyField(Customer)
    lease_start = models.DateField()
    lease_end = models.DateField()
