"""""""""""""""""""""""
django-logging-eventlog
"""""""""""""""""""""""

Logger for the logging module that writes messages to the django database

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
        },
        'loggers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
            'file': {
                'class': 'logging.handlers.FileHandler',
                'filename': 'app.log',
            },
            'root': {
                'handlers': ['file', 'console', 'eventlog'],
                'level': 'INFO',
            },
            'eventlog': {

                'handlers': ['eventlog', ],
                'level': 'INFO',
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
