import uuid

from django.contrib.auth.models import User
from django.db import models

class Classroom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    participants = models.ManyToManyField(User, blank=True, related_name='participants')

    def __str__(self) -> str:
        return f'Classroom: {self.name}'

class Homework(models.Model):
    description = models.TextField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_url = models.URLField(max_length=40, blank=True)

    def __str__(self) -> str:
        return f'Homework: {self.user} -> {self.classroom}'