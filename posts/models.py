from django.db import models
from nie_hub.models import User

# Create your models here.

class Posts(models.Model):
	post_id = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 20)
	date = models.DateTimeField()
	branch = models.CharField(max_length = 3)
	sem = models.IntegerField(null = True)
	user_id=models.ForeignKey(User, on_delete=models.CASCADE)

class attachments(models.Model):
	attachment_id=models.AutoField(primary_key=True)
	link=models.CharField(max_length=50)
	post_id=models.ForeignKey(Posts, on_delete=models.CASCADE)