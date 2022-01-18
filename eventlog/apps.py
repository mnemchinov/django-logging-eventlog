from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EventlogConfig(AppConfig):
    name = 'eventlog'

    def ready(self):
        self.verbose_name = _('Eventlog')
