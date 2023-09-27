from django.apps import AppConfig


class DecoyopsConfig(AppConfig):
    """AppConfig for the DecoyOps Django app.

    This class provides configuration for the DecoyOps app, including the default auto field and the app name.

    Attributes:
        default_auto_field (str): The default auto field for the app's models.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DecoyOps'
