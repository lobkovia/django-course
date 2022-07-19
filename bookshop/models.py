from django.db import models
from django.forms import CharField, IntegerField

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True)
    def __str__(self):
        return f'{self.title} - {self.rating}'


