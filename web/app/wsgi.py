"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
# http://whitenoise.evans.io/en/stable/
# adding whitenoise because wsgi and django do no support static files alone
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = get_wsgi_application()
application = WhiteNoise(application, root='/data/web/static')
application.add_files('/data/web/static', prefix='static/')
