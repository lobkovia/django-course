from django.db import models
from django.forms import CharField, IntegerField

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()


# Create your models here.
