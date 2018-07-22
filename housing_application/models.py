from django.db import models
from accounts.models import Customer
from property.models import Property
from lease.models import Lease


# Create your models here.


class HousingApplication(models.Model):
    class Meta:
        permissions = (
            ('can_set_housing_application_status', 'Change housing application status'), )

    date_application_submitted = models.DateTimeField()
    lease = models.ManyToManyField(Lease)
    property = models.ForeignKey(Property, on_delete=models.PROTECT, default='380a0e1e-95ae-4863-8b75-d2cef6d41b18')

    APPLICATION_STATUS_OPTIONS = (
        ('APPLIED', 'Submitted'),
        ('IN_REVIEW', 'In review'),
        ('DENIED', 'Denied'),
        ('APPROVED', 'Approved'),
    )

    application_status = models.CharField(max_length=15, choices=APPLICATION_STATUS_OPTIONS,
                                          default='APPLIED')









