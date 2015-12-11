#!/usr/bin/env python
import os
import sys

from django.conf import settings
from django.core.management import call_command

BASE_DIR = os.path.dirname(__file__)


def runtests():
    if not settings.configured:
        # Configure test environment
        settings.configure(
            INSTALLED_APPS=(
                'django.contrib.contenttypes',
                'static_pages',
            ),
            ROOT_URLCONF='static_pages.tests.urls',
            STATIC_PAGES_LIST=(
                ('/', 'index.html'),
                ('about_name', 'about.html'),
            ),
            STATIC_PAGES_DIR=os.path.join(os.path.abspath(BASE_DIR), 'html'),
        )

    try:
        # Django 1.9
        from django import setup
    except ImportError:
        setup = None
    if setup is not None:
        setup()

    failures = call_command('test', 'static_pages', interactive=False, failfast=False, verbosity=1)
    sys.exit(bool(failures))


if __name__ == '__main__':
    runtests()
