from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Signup(AbstractUser):
	"""docstring for Signup"""
	seller = 'SR'
	buyer = 'BR'
	avilable_permission=(('SR','seller'),('BR','buyer'))
	User_type = models.CharField(max_length=2,choices=avilable_permission)


class ItemDetails(models.Model):
	Upload_image = models.ImageField(upload_to = 'shopping_app/images')
	Discription = models.TextField(max_length=500)
	Price = models.IntegerField()

class Registration(models.Model):
	username = models.ForeignKey(Signup,on_delete = models.CASCADE)
	key = models.CharField(max_length=100)


'''class ShoppingSignup(AbstractUser):
	name = models.CharField(max_length=100, blank=True, null=True)
'''
	

