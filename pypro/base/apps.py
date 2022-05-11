from django.apps import AppConfig

from pypro import base


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pypro.base'
