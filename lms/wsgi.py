"""
WSGI config for lms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/Users/anastasiatokareva/Documents/Coding/PyCharm/LMS_Hillel/Hillel-LMS-Project')
sys.path.append('/Users/anastasiatokareva/Documents/Coding/PyCharm/LMS_Hillel/Hillel-LMS-Project/lms')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms.settings')

application = get_wsgi_application()
