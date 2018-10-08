from django.db import models
from django.utils import timezone

class User(models.Model):
	uid = models.AutoField(primary_key = True)
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	branch = models.CharField(max_length = 3)
	sem = models.IntegerField()
	address = models.TextField()
	email = models.CharField(max_length = 30)
	phone_number = models.IntegerField()
	usn = models.CharField(max_length = 10)
	password = models.CharField(max_length = 20)
	category = models.CharField(max_length = 10)