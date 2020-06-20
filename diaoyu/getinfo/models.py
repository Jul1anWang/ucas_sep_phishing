from django.db import models
from django import forms
# Create your models here.


class Info(models.Model):
    username = models.CharField(max_length=40, verbose_name="username")
    pwd = models.CharField(max_length=40, verbose_name="pwd")

    def __str__(self):
        return self.username