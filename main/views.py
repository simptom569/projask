from django.shortcuts import render


def main(request):
	return render(request, 'main/main.html')


def about(request):
	return render(request, 'main/about.html')