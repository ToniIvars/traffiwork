from django.contrib import admin
from django.urls import include, path

from .views import landing

urlpatterns = [
    path('', landing, name='landing'),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('classrooms/', include('classrooms.urls')),
    path('students/', include('students.urls')),
]
