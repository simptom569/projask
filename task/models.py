from django.db import models


class TasksForId(models.Model):
	user_id = models.AutoField(primary_key=True)