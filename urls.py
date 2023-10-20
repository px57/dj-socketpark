# chat/routing.py

from django.urls import re_path
from .consumers import InternalConsumer
from .libs import create_websocket_urlparttern

websocket_urlpatterns = create_websocket_urlparttern()

# [
    # re_path("ws/internal/", InternalConsumer.as_asgi()),
    # re_path("ws/playroom/$", PlayRoomConsumer.as_asgi()),
    # re_path("ws/chatroom/$", ChatRoomConsumer.as_asgi()),
    # re_path("ws/victory_talk/$", VictoryTalkConsumer.as_asgi()),
# ]