.. image:: https://img.shields.io/github/license/mnemchinov/django-logging-eventlog   :alt: GitHub

"""""""""""""""""""""""
django-logging-eventlog
"""""""""""""""""""""""

Logger for the logging module that writes messages to the django database


.. image:: http://www.mnemchinov.ru/images/projects/django-logging-eventlog/eventlog_events.jpg

.. image:: http://www.mnemchinov.ru/images/projects/django-logging-eventlog/eventlog_exception.jpg

------------
Installation
------------

#) Install using pip::

    pip install --upgrade django-logging-eventlog

#) Modify your ``settings.py``. Add ``eventlog`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        #django apps
        'eventlog',
        #your apps
    ]

#) Configure ``LOGGING`` in your ``settings.py`` for example::

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'eventlog': {
                'class': 'eventlog.services.EventLogHandler'
            },
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'root': {
                'handlers': ['console', 'eventlog'],
                'level': 'INFO',
                'propagate': True,
            },
        }
    }

#) Run ``python manage.py makemigrations eventlog`` and run Run ``python manage.py migrate``

-----
Usage
-----

.. code-block:: python

    import logging

    logger = logging.getLogger(__name__)
    logger.info('info')
    logger.debug('debug')
    logger.error('error')
    logger.critical('critical')
    logger.warning('warning')

    try:
        1/0

    except Exception as ex:
        logger.exception(ex, exc_info=ex)

To prune the eventlog, use the command as ``pruneeventlog``.
For example, to keep records in the database only for the last 30 days, run::

    python manage.py pruneeventlog 30

