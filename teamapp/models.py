from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teams = models.ManyToManyField('Team', related_name='members')


class Team(models.Model):
    name = models.CharField(max_length=100)