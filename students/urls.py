from django.urls import path

from . import views

urlpatterns = [
    path('me', views.dashboard, name='dashboard'),
]