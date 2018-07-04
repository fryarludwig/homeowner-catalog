from django.apps import AppConfig


class RentplusApiConfig(AppConfig):
    name = 'homeowner_catalog'
    verbose_name = 'Homeowner Catalog'

    def ready(self):
        import homeowner_catalog.signals.handlers
