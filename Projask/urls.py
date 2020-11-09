from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('task', include('task.urls')),
    path('auth/', include('authentication.urls')),
]
