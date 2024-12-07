from django.db import models

# Create your models here.

class Todo(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    # status = models.BooleanField()
