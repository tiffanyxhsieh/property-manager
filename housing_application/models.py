from django.db import models
from customer_account.models import Customer
# Create your models here.


class HousingApplication(models.Model):
    date_application_submitted = models.DateTimeField()
    applicants = models.ManyToManyField(Customer)
    lease_start = models.DateField()

    LEASE_DURATION_OPTIONS = (
        ('6', '6 Months'),
        ('8', '8 Months'),
        ('12', '12 Months'),
        ('15', '15 Months'),
    )

    lease_duration = models.CharField(max_length=2, choices=LEASE_DURATION_OPTIONS, blank=True, default='12',
                                      help_text='Lease Duration')

    APPLICATION_STATUS_OPTIONS = (
        ('APPLIED', 'Submitted'),
        ('IN_REVIEW', 'In review'),
        ('DENIED', 'Denied'),
        ('APPROVED', 'Approved'),
    )

    application_status = models.CharField(max_length=15, choices=APPLICATION_STATUS_OPTIONS)