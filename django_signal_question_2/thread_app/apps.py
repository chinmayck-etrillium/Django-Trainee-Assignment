from django.apps import AppConfig


class ThreadAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'thread_app'

    def ready(self):
        import thread_app.threads