import uuid

from django.contrib.auth.models import User
from django.db import models

class Classroom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, verbose_name='Nombre')
    description = models.TextField(blank=True, verbose_name='Descripción')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    participants = models.ManyToManyField(User, blank=True, related_name='participants')

    def __str__(self) -> str:
        return f'Classroom: {self.name} ({self.creator})'