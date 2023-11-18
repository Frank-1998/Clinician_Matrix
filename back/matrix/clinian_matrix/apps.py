from django.apps import AppConfig


class ClinianMatrixConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clinian_matrix'
    def ready(self) -> None:
        import clinian_matrix.signals
        