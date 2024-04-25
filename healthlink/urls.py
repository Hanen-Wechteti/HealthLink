from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('tasks/', include('tasks.urls')),
    path('admin/', admin.site.urls),
]
