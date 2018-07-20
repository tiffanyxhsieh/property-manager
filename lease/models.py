from django.db import models
from property.models import Property
from accounts.models import Employee
from accounts.models import Customer

# Create your models here.
class Lease(models.Model):

    start_date = models.DateField
    property = models.ForeignKey(Property, on_delete=models.PROTECT)

    LEASE_DURATION_OPTIONS = (
        (6, '6 Months'),
        (8, '8 Months'),
        (12, '12 Months'),
        (15, '15 Months'),
    )
    applicants = models.ManyToManyField(Customer)
    duration = LEASE_DURATION_OPTIONS
    monthly_rent = models.FloatField
    monthly_fees = models.FloatField
    approved_by = models.ForeignKey(Employee, on_delete=models.PROTECT)
    date_approved = models.DateField

