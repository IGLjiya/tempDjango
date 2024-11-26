from django.db import models

# Create your models here.

class Todo(models.Model):
    sino = models.IntegerField()
    date = models.DateField()
    task = models.CharField(max_length=30)
    status = models.BooleanField()
