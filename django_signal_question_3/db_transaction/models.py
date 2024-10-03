from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=25)
    model = models.CharField(max_length=25)

class LogEntry(models.Model):
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
