from django.db import models
from django.contrib.auth import models as a_models

class Task(models.Model):
    creator = a_models.User()
    users = models.ManyToManyField(a_models.User)
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=1000)
    end_date = models.DateTimeField()
    
    def __str__(self):
        return self.name