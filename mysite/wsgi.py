"""
James Wong <jameshsw@gmail.com>

WSGI config
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
