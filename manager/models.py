from django.db import models
from register.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    mobile_number = PhoneNumberField(null=False, blank=False, unique=True)