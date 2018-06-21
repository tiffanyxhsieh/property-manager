from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#TODO: change app to just "accounts"
#TODO: add "staff" and "admin/manager" users


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()


#TODO: split into leasing employee and maintenance employee?
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=10)



