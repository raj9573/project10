from django.db import models


from django.core import validators

from django.core.validators import *


class user(models.Model):
    name=models.CharField(max_length=100,validators=[validators.MaxLengthValidator(5)])
    surname = models.CharField(max_length=100,default='')
    age = models.IntegerField(default=0)
    qualification = models.CharField(max_length=100,default='')

    


    def __str__(self):
        return self.name

    