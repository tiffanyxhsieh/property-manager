from django.db import models
from housing_application.models import HousingApplication
# Create your models here.


class Property(models.Model):
    address = models.CharField()
    housing_application = models.ForeignKey(HousingApplication)
