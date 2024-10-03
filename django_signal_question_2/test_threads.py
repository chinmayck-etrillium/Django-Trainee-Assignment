import os
import django
import threading

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_signal_question_2.settings')
django.setup()

from thread_app.models import ThreadApp

print(f"Caller is running in thread: {threading.get_ident()}")

ThreadApp.objects.create(thread='run')

print("We can see that the thread_id is same, hence proving that django signals run in the same thread as the caller")
