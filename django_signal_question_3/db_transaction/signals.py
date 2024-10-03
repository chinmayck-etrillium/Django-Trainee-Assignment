from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Car, LogEntry

@receiver(post_save, sender=Car)
def log_car_creation(sender, instance, created, **kwargs):
    if created:
        LogEntry.objects.create(action=f"Created car: {instance.name} {instance.model}")
