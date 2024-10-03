from django.db import models

class MyFirstSignal(models.Model):
    signal = models.CharField(max_length=10)
