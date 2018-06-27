from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    employee_id = models.CharField(max_length=10)
    EMPLOYEE_TYPE = (
                    (1, 'Maintenance'),
                    (2, 'Leasing'),
                    (3, 'Management'),
                    (4, 'Front Desk'),
                   )

    employee_type = models.IntegerField(choices=EMPLOYEE_TYPE, default=4)
    ss_number = models.IntegerField(default=1)
    id_number = models.IntegerField(default=2)



