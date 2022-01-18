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
    version='0.0.2',
    use_scm_version={"local_scheme": local_scheme} if os.getenv('TestPypi') == 'yes' else False,  # using `setuptools_scm` when publish to test.pypi
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
        'Environment :: Web Environment',
        'Framework :: Django',
	'Framework :: Django :: 3.0',	
	'Framework :: Django :: 3.1',	
	'Framework :: Django :: 3.2',	
	'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
    ],
)
