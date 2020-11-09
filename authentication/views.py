from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from task.models import Users
from .forms import SignInForm, SignUpForm


def auth(request):
	if request.user.is_authenticated:
		return redirect('main')
	return redirect('sign_in')


def sign_in(request):
	if request.user.is_authenticated:
		return redirect('main')
	error = ''
	if request.method == 'POST':
		form = SignInForm(request.POST)
		if form.is_valid():
			try:
				sign_user = Users.objects.get(user_id=request.POST['user_id'])
				print(sign_user.user_password)
				if sign_user.user_password == request.POST['user_password']:
					user_name = User.objects.get(id=sign_user.user_id).username
					sign_user = authenticate(request, username=user_name, password=sign_user.user_password)
					login(request, sign_user)
					return redirect('main')
				else:
					error = 'Wrong password'
			except Users.DoesNotExist:
				error = 'User does not exist'
	form = SignInForm()
	context = {
	'form': form,
	'error': error,
	}
	return render(request, 'authentication/sign_in.html', context)


def sign_up(request):
	if request.user.is_authenticated:
		return redirect('main')
	error = ''
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			user = User.objects.create_user(username=request.POST['user_name'], password=request.POST['user_password'])
			user = authenticate(request, username=request.POST['user_name'], password=request.POST['user_password'])
			login(request, user)
	form = SignUpForm()
	context = {'form': form}
	return render(request, 'authentication/sign_up.html', context)


def sign_out(request):
	if request.user.is_authenticated:
		logout(request)
	return redirect('main')