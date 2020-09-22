from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    description = models.CharField(max_length=255, null=False, blank=False)
    done = models.BooleanField(null=False, default=False)
    date = models.DateField(null=False)
    deleted = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
