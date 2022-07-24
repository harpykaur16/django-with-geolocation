from django.apps import AppConfig


class BasicMeasurementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basic_measurements'
    verbose_name = 'Measurement between 2 locations'
