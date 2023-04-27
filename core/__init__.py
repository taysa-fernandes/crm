from django.apps import apps
from django.core.exceptions import AppRegistryNotReady
from .backends import EmailBackend

try:
    backend = EmailBackend()
except AppRegistryNotReady:
    config = apps.get_app_config('<core>')
    config.ready()
    backend = EmailBackend()