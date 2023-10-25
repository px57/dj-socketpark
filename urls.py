# chat/routing.py

from django.urls import re_path
from .consumers import InternalConsumer
from .libs import create_websocket_urlparttern

websocket_urlpatterns = create_websocket_urlparttern()
