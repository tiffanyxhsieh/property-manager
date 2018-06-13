from django.db import models

# Create your models here.


class Customer(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=100)
    date_of_birth = models.DateField()




