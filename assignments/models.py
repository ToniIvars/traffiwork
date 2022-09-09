import uuid

from django.contrib.auth.models import User
from django.db import models

from classrooms.models import Classroom

# Create your models here.
class Assignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_url = models.URLField(max_length=40, blank=True)

    def __str__(self) -> str:
        return f'Assignment: {self.user} -> {self.classroom}'