import django
import os
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_signal_question_1.settings')
django.setup()


from first_signal.models import MyFirstSignal

book = MyFirstSignal.objects.create(signal="run")

print("Process complete.")
print("We can see that when the sleep is introduced signals.py the execution waits and after that it completes the 'Process complete', which proves that django signals are executed synchronously ")
