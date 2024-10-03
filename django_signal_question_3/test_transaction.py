import os
import django
from django.db import transaction


# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_signal_question_3.settings')
django.setup()


from db_transaction.models import Car, LogEntry

def test_transaction_behavior():
    try:
        with transaction.atomic():
            car = Car.objects.create(name='XC90', model='Volvo')
            print("Car created:", car.name)

            log_entries = LogEntry.objects.all()
            print("Log entries count before rollback:", log_entries.count())

            raise Exception("Rolling back transaction")

    except Exception as e:
        print("Caught exception:", e)

    log_entries_after = LogEntry.objects.all()
    print("Log entries count after rollback:", log_entries_after.count())


test_transaction_behavior()
