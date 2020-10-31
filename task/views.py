from django.shortcuts import render
from .forms import CreateTaskForm
from .models import Task


def tasks(request):
	return render(request, 'task/tasks.html')


def create(request):
	if request.method == 'POST':
		form = CreateTaskForm(request.POST)
		if form.is_valid():
			form.save()
	form = CreateTaskForm()
	context = {'form': form}
	return render(request, 'task/create.html', context)


def task(request, pk):
	task = Task.objects.get(task_id=pk)
	task_id = task.task_id
	task_password = task.task_password
	context = {
	'id': task_id,
	'password': task_password,
	}
	return render(request, 'task/task.html', context)