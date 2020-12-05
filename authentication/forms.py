from django import forms
from task.models import Users


class SignUpForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ['user_name', 'user_password']
		widgets = {
		'user_password': forms.TextInput(attrs={
		'class': 'sign_up',
		'placeholder': 'password',
		'autocomplete': 'off',
		}),
		'user_name': forms.TextInput(attrs={
		'class': 'sign_up',
		'placeholder': 'name',
		'autocomplete': 'off',
		}),
		}


class SignInForm(forms.Form):
	user_password = forms.CharField(widget=forms.TextInput(attrs={
	'class': 'sign_in',
	'placeholder': 'password',
	}))
	user_name = forms.CharField(widget=forms.TextInput(attrs={
	'class': 'sign_in',
	'placeholder': 'name',
	}))