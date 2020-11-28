from django.db import models
from django.utils import timezone
from uuid import uuid4


class Task(models.Model):
	task_id = models.CharField(primary_key=True, default=uuid4, max_length=50)
	task_name = models.CharField(max_length=50)
	task_password = models.CharField(default=None, max_length=50)
	
	def __str__(self):
		return self.task_id


class Users(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_password = models.CharField(max_length=50)
	user_task = models.ManyToManyField(Task, blank=True)
	
	def __str__(self):
		return str(self.user_id)


class Messages(models.Model):
	id = models.CharField(primary_key=True, default=uuid4, max_length=50)
	message = models.TextField()
	author = models.ForeignKey(Users)
	task = models.ForeignKey(Task)
	reply = models.ForeignKey(Messages)
	date = models.DateTimeField(default=timezone.now)