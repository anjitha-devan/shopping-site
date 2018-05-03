from django.db import models

# Create your models here.
class Signup(models.Model):
	"""docstring for Signup"""
	seller = 'SR'
	buyer = 'BR'
	avilable_permission=(('SR','seller'),('BR','buyer'))
	your_name = models.CharField(max_length=100)
	email = models.EmailField()
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=20)
	choice = models.CharField(max_length=2,choices=avilable_permission)
