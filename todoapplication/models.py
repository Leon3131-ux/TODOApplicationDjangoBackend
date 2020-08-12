from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, blank=False, default='', null=False)
    description = models.CharField(max_length=255, blank=False, default='', null=False)
    done = models.BooleanField(default=False, null=False)
    date = models.DateField(null=False)
    deleted = models.BooleanField(default=False, null=False)


class User(models.Model):
    username = models.CharField(unique=True, max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
