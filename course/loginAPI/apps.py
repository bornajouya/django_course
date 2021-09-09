from django.apps import AppConfig


class LoginapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loginAPI'

    def ready(self):
        import loginAPI.Signals
