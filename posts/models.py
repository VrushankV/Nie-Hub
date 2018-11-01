from django.db import models
from nie_hub.models import User

# Create your models here.

class Posts(models.Model):
	post_id = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 20)
	body = models.TextField(null = True)
	date = models.DateTimeField(null= True)
	branch = models.CharField(max_length = 3,choices= (('CE','CE'),('CSE','CSE'),('ECE','ECE'),('EEE','EEE'),('ISE','ISE'),('ME','ME'),('IPE','IPE')))
	sem = models.IntegerField(null = False, choices= ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)))
	links = models.FileField(null=True, blank = True)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class attachments(models.Model):
	attachment_id=models.AutoField(primary_key=True)
	link=models.CharField(max_length=50)
	post_id=models.ForeignKey(Posts, on_delete=models.CASCADE)