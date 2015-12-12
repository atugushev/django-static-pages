===================
Django Static Pages
===================

A reusable Django app that generates static pages using Django test client.

.. image:: https://badge.fury.io/py/django-static-pages.png
   :target: http://badge.fury.io/py/django-static-pages

.. image:: https://api.travis-ci.org/atugushev/django-static-pages.png
   :target: https://travis-ci.org/atugushev/django-static-pages

.. image:: https://coveralls.io/repos/atugushev/django-static-pages/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/atugushev/django-static-pages?branch=master

Installation
------------

1. Install a package::

    $ pip install django-static-pages

2. Add "static_pages" to your INSTALLED_APPS setting::

    INSTALLED_APPS = (
        ...
        'static_pages',
    )


Configuration
-------------

Specify which files should be generated as static files::

    STATIC_PAGES_LIST = (
        ('/', 'index.html'),
        ('/about/', 'about.html'),
        ('news:list', 'news/index.html'),
    )

Set path for an output directory of the static files::

    STATIC_PAGES_DIR = '/srv/example.com/html/'

This kwargs will be passed to the Django test client arguments. It may be usefull if you want to
control WSGI environments of the ``RequestFactory`` of the the client::

    STATIC_CLIENT_KWARGS = {
        'HTTP_SERVER_NAME': 'example.com',
    }

Usage
-----

Just execute the following command::

    $ python manage.py generate_static_pages


Requirements
------------

* Python 2.7+ or 3+
* Django>=1.5
