from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Group(models.Model):
    group_name = models.CharField(max_length= 50, null=True)

    def __str__(self) -> str:
        return self.group_name


class User(AbstractUser, models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE,  related_name="user_group", null= True)

