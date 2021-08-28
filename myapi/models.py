# models.py
from django.db import models
class Divar(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    def __str__(self):
        return self.name