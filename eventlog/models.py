from datetime import datetime, timedelta
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.utils.safestring import mark_safe

from eventlog.services import Levels


class EventLevels(models.IntegerChoices):
    notset = Levels.notset.value, Levels.notset.label
    info = Levels.info.value, Levels.info.label
    warning = Levels.warning.value, Levels.warning.label
    debug = Levels.debug.value, Levels.debug.label
    error = Levels.error.value, Levels.error.label
    critical = Levels.critical.value, Levels.critical.label


class EventLogManager(models.Manager):
    def purge(self, days=30):
        return self.filter(
            timestamp__gt=datetime.now() - timedelta(days=days)).delete()


class Event(models.Model):

    id = models.AutoField(primary_key=True)
    initiator = models.CharField(verbose_name=_('Initiator'), max_length=250)
    timestamp = models.DateTimeField(_('Date'), auto_now_add=True)
    level = models.IntegerField(
        verbose_name=_('Level'),
        choices=EventLevels.choices,
        default=0
    )
    event = models.TextField(verbose_name=_('Event'), default="")
    tracing = models.TextField(verbose_name=_('Tracing'), default="")
    objects = EventLogManager()

    class Meta:
        ordering = ('-timestamp',)
        db_table = 'eventlog'
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return f'{self.get_level_display()}: {self.event[:100]}...'

    @property
    def level_label(self):
        event_log_level = [
            level for level in Levels if level[0] == self.level
        ][0]
        label = event_log_level.label
        color = event_log_level.color
        bg_color = event_log_level.bg_color
        style = f'display: inline; padding: .2em .6em .3em; font-size: 75%; ' \
                f'font-weight: bold; text-align: center; white-space: ' \
                f'nowrap; vertical-align: baseline; color: {color}; ' \
                f'background-color: {bg_color}; border-radius: .25em; '
        level_label = f'<span style="{style}">{label}</span>'

        return mark_safe(level_label)
