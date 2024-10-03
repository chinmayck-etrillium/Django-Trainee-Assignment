from django.apps import AppConfig


class DbTransactionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'db_transaction'

    def ready(self):
        import db_transaction.signals
