bmprototype
===========

Django Demo deployment to render


## Running development server

`` python

	...\> py manage.py runserver

``

## Running Django in Gunicorn as a generic WSGI application¶

When Gunicorn is installed, a gunicorn command is available which starts the Gunicorn server process. The simplest invocation of gunicorn is to pass the location of a module containing a WSGI application object named application, which for a typical Django project would look like:

`` python

	gunicorn myproject.wsgi

``
