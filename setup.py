import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def local_scheme(version):
    return ""


setup(
    name='django-logging-eventlog',
    version=__import__('eventlog').__version__,
    setup_requires=['setuptools_scm'],
    packages=['eventlog', 'eventlog.migrations'],
    include_package_data=True,
    license='MIT License',
    description='Logger for the logging module that writes messages to the database',
    long_description=README,
    url='https://github.com/mnemchinov/django-logging-eventlog',
    author='mnemchinov',
    author_email='mnemchinov@mail.ru',
    install_requires=['django>=3.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
)
