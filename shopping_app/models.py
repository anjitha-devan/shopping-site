from django.db import models

# Create your models here.
class Signup(models.Model):
	"""docstring for Signup"""
	seller = 'SR'
	buyer = 'BR'
	avilable_permission=(('SR','seller'),('BR','buyer'))
	Name = models.CharField(max_length=100)
	Email = models.EmailField()
	Username = models.CharField(max_length=50)
	Password = models.CharField(max_length=20)
	User_type = models.CharField(max_length=2,choices=avilable_permission)
class ItemDetails(models.Model):
	Upload_image = models.ImageField(upload_to = 'shopping_app/images')
	Discription = models.TextField(max_length=500)
	Price = models.IntegerField()

