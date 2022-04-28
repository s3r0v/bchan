from django.db import models
import datetime

# Create your models here.
class BoardModel(models.Model):
	title = models.CharField(max_length=1024, default='')
	description = models.CharField(max_length=1024, default='')
	link = models.CharField(max_length=4, default='')

class ThreadModel(models.Model):
	content = models.CharField(max_length=1024, default='')	
	date_published = models.DateField(default=datetime.date.today())
	board = models.ForeignKey(BoardModel, on_delete=models.CASCADE)

class PostModel(models.Model):
	content = models.CharField(max_length=1024, default='')	
	date_published = models.DateField(default=datetime.date.today())
	board = models.ForeignKey(ThreadModel, on_delete=models.CASCADE)