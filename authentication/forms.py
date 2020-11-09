from django import forms
from task.models import Users


class SignUpForm(forms.ModelForm):
	user_name = forms.CharField(widget=forms.TextInput(attrs={
	'class': 'sign_up',
	'placeholder': 'name',
	'autocomplete': 'off',
	}))
	class Meta:
		model = Users
		fields = ['user_password']
		widgets = {
		'user_password': forms.TextInput(attrs={
		'class': 'sign_up',
		'placeholder': 'password',
		'autocomplete': 'off',
		}),
		}


class SignInForm(forms.Form):
	user_id = forms.CharField(widget=forms.TextInput(attrs={
	'class': 'sign_in',
	'placeholder': 'id',
	}))
	user_password = forms.CharField(widget=forms.TextInput(attrs={
	'class': 'sign_in',
	'placeholder': 'password',
	}))
	user_name = forms.CharField(widget=forms.TextInput(attrs={
	'class': 'sign_in',
	'placeholder': 'name',
	}))