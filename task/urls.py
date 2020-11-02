from django.urls import path
from . import views


urlpatterns = [
	path('', views.tasks, name='tasks'),
	path('/create', views.create, name='create'),
	path('/id/<pk>', views.task, name='task'),
	path('/connect', views.connect, name='connect'),
	#path('/connect/<pk>', views.connect_id, name='connect_id')
	]