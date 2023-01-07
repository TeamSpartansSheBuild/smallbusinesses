from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    host = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=1000, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)