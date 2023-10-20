# chat/routing.py
from django.urls import re_path

from socketpark.consumers import InternalConsumer
from playroom.consumers import PlayRoomConsumer
from chatroom.consumers import ChatRoomConsumer
from victory_talk.consumers import VictoryTalkConsumer

websocket_urlpatterns = [
    re_path("ws/internal/", InternalConsumer.as_asgi()),
    re_path("ws/playroom/$", PlayRoomConsumer.as_asgi()),
    re_path("ws/chatroom/$", ChatRoomConsumer.as_asgi()),
    re_path("ws/victory_talk/$", VictoryTalkConsumer.as_asgi()),
]