from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Signup(AbstractUser):
    """docstring for Signup"""
    seller = 'SR'
    buyer = 'BR'
    avilable_permission = (('SR', 'seller'), ('BR', 'buyer'))
    User_type = models.CharField(max_length=2, choices=avilable_permission)


class ItemDetails(models.Model):
    user = models.ForeignKey(Signup, on_delete=models.CASCADE, null=True, blank=True)
    Upload_image = models.ImageField(upload_to='shopping_app/images')
    Product_name = models.TextField(max_length=25)
    Discription = models.TextField(max_length=500)
    Price = models.IntegerField(default=0)

    def __str__(self):
        return self.Product_name


class Registration(models.Model):
    user = models.ForeignKey(Signup, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
