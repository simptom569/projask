from django.urls import path
from . import views


urlpatterns = [
	path('', views.task, name='task'),
	path('/create', views.create, name='create')
	]