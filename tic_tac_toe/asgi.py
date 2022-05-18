"""
ASGI config for tic_tac_toe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tic_tac_toe.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": AsgiHandler()
})
