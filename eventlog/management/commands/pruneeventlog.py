import logging

from django.core.management.base import BaseCommand
from eventlog.services import EventLogHandler


class Command(BaseCommand):
    help = 'Deletes entries from the eventlog older than the specified ' \
           'number of days'

    def add_arguments(self, parser):
        parser.add_argument(
            'days',
            type=int,
            help='The number of days to prune the eventlog',
        )

    def handle(self, *args, **options):
        days = options['days']
        logger = logging.getLogger(__name__)

        try:
            event_log = EventLogHandler()
            count = event_log.prune(days)
            print('1')
            logger.info(f'The eventlog have been pruned to {days} day(s) and'
                        f' {count} row(s) have been deleted')

        except Exception as ex:
            logger.exception(ex, exc_info=ex)


