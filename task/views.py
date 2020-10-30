from django.shortcuts import render


def tasks(request):
	return render(request, 'task/tasks.html')


def create(request):
	return render(request, 'task/create.html')


def task(request, pk):
	return render(request, 'task/task.html')