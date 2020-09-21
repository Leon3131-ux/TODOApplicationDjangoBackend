from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255, blank=False, default='', null=False, unique=True)
    description = models.CharField(max_length=255, blank=False, default='', null=False)
    done = models.BooleanField(default=False, null=False)
    date = models.DateField(null=False)
    deleted = models.BooleanField(default=False, null=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
