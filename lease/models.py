from django.db import models
from property.models import Property
from accounts.models import Employee
from accounts.models import Customer

# Create your models here.
class Lease(models.Model):

    start_date = models.DateField(null=True, blank=True)
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    is_approved = models.BooleanField(default=False)

    LEASE_DURATION_OPTIONS = (
        (6, '6 Months'),
        (8, '8 Months'),
        (12, '12 Months'),
        (15, '15 Months'),
    )
    applicants = models.ManyToManyField(Customer)
    duration = models.IntegerField(choices=LEASE_DURATION_OPTIONS, default=6)
    monthly_rent = models.DecimalField(decimal_places=2, max_digits=9, default=1000.00)
    monthly_fees = models.DecimalField(decimal_places=2, max_digits=7, default=100.00)
    #TODO:fix approved_by field.....getting null errors
    #approved_by = models.ForeignKey(Employee, on_delete=models.PROTECT)
    date_approved = models.DateTimeField(null=True, blank=True)


