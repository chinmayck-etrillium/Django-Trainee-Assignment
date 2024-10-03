import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ThreadApp
import time

@receiver(post_save, sender=ThreadApp)
def post_save_handler(sender, instance, **kwargs):
    print(f"Current thread is: {threading.get_ident()}")
