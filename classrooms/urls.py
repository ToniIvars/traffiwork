from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add, name='add_classroom'),
    path('join/<id>', views.join, name='join_classroom')
]