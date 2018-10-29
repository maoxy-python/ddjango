"""
WSGI config for ddjango project.  web application   内置的web server 来运行application
# django内置的服务器是遵循了wsgi协议实现的
It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
#
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ddjango.settings')

application = get_wsgi_application()
