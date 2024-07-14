from django.apps import AppConfig


class AuthtokenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authtoken'
    verbose_name = "Auth Token"

    def ready(self):
        import authtoken.signals