"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application  # Corrected spelling

# Determine which settings module to use
setting_module = "myproject.deployment" if "RENDER_EXTERNALHOSTNAME" in os.environ else "myproject.settings"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting_module)

# Corrected spelling for get_wsgi_application
application = get_wsgi_application()
