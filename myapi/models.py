from typing import FrozenSet
from django.db import models
from django.db.models import CharField, IntegerField, ForeignKey, CASCADE, ManyToManyField

# Create your models here.

class Author(models.Model):
    name = CharField(max_length=100)
    age = IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'