from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    ss_number = models.IntegerField(default=1)

    def __str__(self):
        return '({0} {1} {2})'.format(self.user.first_name, self.user.last_name, self.user_id)


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

    def __str__(self):
        return '({0} {1} {2})'.format(self.user.first_name, self.user.last_name, self.user_id)



