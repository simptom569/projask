from django.shortcuts import render


def task(request):
	return render(request, 'task/task.html')


def create(request):
	return render(request, 'task/create.html')