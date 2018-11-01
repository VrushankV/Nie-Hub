from django.db import models

class User(models.Model):
	uid = models.AutoField(primary_key = True)
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20, null= True)
	branch = models.CharField(max_length = 3,choices= (('CE','CE'),('CSE','CSE'),('ECE','ECE'),('EEE','EEE'),('ISE','ISE'),('ME','ME'),('IPE','IPE')))
	sem = models.IntegerField(null = True)
	address = models.TextField(null=True)
	email = models.CharField(max_length = 30)
	phone_number = models.IntegerField(max_length = 10)
	usn = models.CharField(max_length = 10)
	password = models.CharField(max_length = 20)
	category = models.CharField(max_length = 10)
