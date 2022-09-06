from django.contrib import admin

from .models import Classroom, Homework

admin.site.register(Classroom)
admin.site.register(Homework)