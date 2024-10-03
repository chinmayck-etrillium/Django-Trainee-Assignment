from django.db import models

class ThreadApp(models.Model):
    thread = models.CharField(max_length=10)