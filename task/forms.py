from django import forms
from .models import Task


class CreateTask(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['task_password']
		widgets = {
		'task_password': forms.TextInput(attrs={
		'class': 'password',
		}),
		}