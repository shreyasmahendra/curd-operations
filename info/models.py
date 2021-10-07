from django.db import models
from register.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)