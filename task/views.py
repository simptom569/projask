from django.shortcuts import render
from .forms import CreateTaskForm


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
	return render(request, 'task/task.html')