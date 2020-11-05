from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from .forms import CreateTaskForm, ConnectionToTaskForm, ConnectionToTaskIdForm
from .models import Task, Users


def tasks(request):
	user = request.user.id
	try:
		user = Users.objects.get(user_id=user)
	except:
		user = Users(user_id=user, user_password='12345')
		user.save()
	user = user.user_task.all()
	context = {'task': user}
	return render(request, 'task/tasks.html', context)


def create(request):
	if request.method == 'POST':
		form = CreateTaskForm(request.POST)
		if form.is_valid():
			form = form.save()
			user = Users.objects.get(user_id=request.user.id)
			user.user_task.add(form)
	form = CreateTaskForm()
	context = {'form': form}
	return render(request, 'task/create.html', context)


def task(request, pk):
	if request.user.is_anonymous:
		return redirect('main')
	try:
		task = Task.objects.get(task_id=pk)
		task_id = task.task_id
		user = Users.objects.get(user_id=request.user.id)
		user = user.user_task.values_list('task_id', flat=True)
		if not task_id in user:
			return redirect('connect_id', pk=pk)
		task_password = task.task_password
		context = {
		'id': task_id,
		'password': task_password,
		}
	except Task.DoesNotExist:
		raise Http404("Task does not exist")
	return render(request, 'task/task.html', context)


def connect(request):
	error = ''
	if request.method == 'POST':
		form = ConnectionToTaskForm(request.POST)
		if form.is_valid():
			try:
				task = Task.objects.get(task_id=request.POST['task_id'])
				if task.task_password == request.POST['task_password']:
					user = Users.objects.get(user_id=request.user.id)
					user.user_task.add(task)
				else:
					error = 'Wrong password'
			except Task.DoesNotExist:
				error = 'Task does not exist'
	form = ConnectionToTaskForm()
	context = {
	'form': form,
	'error': error,
	}
	return render(request, 'task/connect.html', context)


def connect_id(request, pk):
	pk = pk
	error = ''
	if request.method == 'POST':
		form = ConnectionToTaskIdForm(request.POST)
		if form.is_valid():
			try:
				task = Task.objects.get(task_id=pk)
				if task.task_password == request.POST['task_password']:
					user = Users.objects.get(user_id=request.user.id)
					user.user_task.add(task)
					return redirect('task', pk=pk)
				else:
					error = 'Wrong password'
			except Task.DoesNotExist:
				error = 'Task does not exist'
	form = ConnectionToTaskIdForm()
	context = {
	'form': form,
	'error': error,
	}
	return render(request, 'task/connect_id.html', context)