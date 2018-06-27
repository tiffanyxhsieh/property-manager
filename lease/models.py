from django.db import models
from property.models import Property
from accounts.models import Employee

# Create your models here.
class Lease(models.Model):

    start_date = models.DateField
    property = models.ForeignKey(Property)

    LEASE_DURATION_OPTIONS = (
        (6, '6 Months'),
        (8, '8 Months'),
        (12, '12 Months'),
        (15, '15 Months'),
    )
    duration = LEASE_DURATION_OPTIONS
    monthly_rent = models.FloatField
    monthly_fees = models.FloatField
    approved_by = models.ForeignKey(Employee)
    date_approved = models.DateField

