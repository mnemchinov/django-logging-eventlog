import logging
from collections import namedtuple
from django.utils import timezone

from django.apps import apps

# region Levels

_Level = namedtuple('_Level', 'value label color bg_color')
notset = _Level(
    logging.NOTSET,
    logging.getLevelName(logging.NOTSET),
    '#fff',
    '#3498db'
)
info = _Level(
    logging.INFO,
    logging.getLevelName(logging.INFO),
    '#fff',
    '#62cb31'
)
warning = _Level(
    logging.WARNING,
    logging.getLevelName(logging.WARNING),
    '#fff',
    '#ffb606'
)
debug = _Level(
    logging.DEBUG,
    logging.getLevelName(logging.DEBUG),
    '#fff',
    '#6a6c6f'
)
error = _Level(
    logging.ERROR,
    logging.getLevelName(logging.ERROR),
    '#fff',
    '#e74c3c'
)
critical = _Level(
    logging.CRITICAL,
    logging.getLevelName(logging.CRITICAL),
    '#fff',
    '#c0392b'
)

_Levels = namedtuple(
    '_Levels',
    'notset, info, warning, debug, error, critical'
)
Levels = _Levels(notset, info, warning, debug, error, critical)

# endregion

APP_NAME = 'eventlog'
APP_MODEL_EVENT_NAME = 'Event'


class EventLogHandler(logging.Handler):

    @staticmethod
    def prune(days: int):
        event_model = apps.get_model(APP_NAME, APP_MODEL_EVENT_NAME)
        date_time = timezone.now() - timezone.timedelta(days=days)
        rows_to_prune = event_model.objects.filter(timestamp__lte=date_time)
        count = rows_to_prune.count()
        rows_to_prune.delete()

        return count

    def emit(self, record):
        event_model = apps.get_model(APP_NAME, APP_MODEL_EVENT_NAME)
        trace = ""

        if record.exc_info:
            db_default_formatter = logging.Formatter()
            trace = db_default_formatter.formatException(record.exc_info)

        event = record.getMessage()
        event_model.objects.create(
            initiator=record.name,
            level=record.levelno,
            event=event,
            tracing=trace
        )
