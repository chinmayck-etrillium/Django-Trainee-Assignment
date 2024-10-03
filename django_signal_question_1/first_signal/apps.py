from django.apps import AppConfig


class FirstSignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'first_signal'

    def ready(self):
        import first_signal.signals
