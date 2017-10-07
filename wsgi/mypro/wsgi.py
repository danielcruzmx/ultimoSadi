"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/Users/danielcruzmx/sadicarnot/ultimoSadi/wsgi/mypro/myproject')
sys.path.append('/Users/danielcruzmx/sadicarnot/ultimoSadi/wsgi/mypro')

os.environ["DJANGO_SETTINGS_MODULE"] = "myproject.settings"


# GETTING-STARTED: change 'myproject' to your project name:
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wsgi_application()
