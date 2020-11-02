from django import forms
from .models import Task


class CreateTaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['task_id', 'task_name', 'task_password']
		widgets = {
		'task_password': forms.TextInput(attrs={
		'class': 'create_task',
		'placeholder': 'password',
		'autocomplete': 'off',
		}),
		'task_id': forms.TextInput(attrs={
		'class': 'create_task',
		'readonly': 'readonly',
		}),
		'task_name': forms.TextInput(attrs={
		'class': 'create_task',
		'placeholder': 'name',
		'autocomplete': 'off',
		}),
		}


class ConnectionToTaskForm(forms.Form):
	task_id = forms.CharField(widget=forms.TextInput(attrs={
	'placeholder': 'id',
	'class': 'connect_task',
	'autocomplete': 'off'
	}))
	task_password = forms.CharField(widget=forms.TextInput(attrs={
	'placeholder': 'password',
	'class': 'connect_task',
	'autocomplete': 'off'
	}))