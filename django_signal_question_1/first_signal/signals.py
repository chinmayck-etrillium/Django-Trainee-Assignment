from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyFirstSignal
import time

@receiver(post_save, sender=MyFirstSignal)
def post_save_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    time.sleep(2)
    print("Signal handler finished.")
