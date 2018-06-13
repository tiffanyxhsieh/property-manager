from django.db import models

# Create your models here.

class HousingApplication(models.Model):
    date_submitted = models.DateTimeField()
    #property_applied_for = models.ForeignKey()
