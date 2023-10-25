
from kernel.commandline.print import print_title
from kernel.websocket.config import find_consumers_files
from django.urls import re_path


def convert_camelcase_to_snakecase(name: str):
    """
        @description: convert CamelCase to snake_case
    """
    return ''.join(['_'+i.lower() if i.isupper() else i for i in name]).lstrip('_')

def yield__websocket_urlparttern():
    """
        @description:  yield all websocket urlpartterns
    """
    pathname_list = {}
    consumers_file = find_consumers_files()
    for consumer_file in consumers_file:
        for consumer in dir(consumer_file.consumers):
            if not hasattr(getattr(consumer_file.consumers, consumer), "as_asgi"):
                continue
    
            pathname = convert_camelcase_to_snakecase(consumer)
            if pathname in pathname_list:
                raise Exception(f"The consumer {pathname} is duplicated in {pathname_list[pathname]} and {consumer_file}")
            yield consumer, consumer_file

def create_websocket_urlparttern():
    """
        @description:
        @return: 
            [
                re_path("ws/internal/", InternalConsumer.as_asgi()),
                re_path("ws/playroom/$", PlayRoomConsumer.as_asgi()),
                re_path("ws/chatroom/$", ChatRoomConsumer.as_asgi()),
                re_path("ws/victory_talk/$", VictoryTalkConsumer.as_asgi()),
            ] 
    """
    urlpartterns = []
    consumers_file = find_consumers_files()
    for consumer, consumer_file in yield__websocket_urlparttern():
        pathname = convert_camelcase_to_snakecase(consumer)
        urlpartterns.append(
            re_path(
                f"ws/{pathname}/$", 
                getattr(consumer_file.consumers, consumer).as_asgi()
            )
    )
    show_url_partterns(urlpartterns)
    return urlpartterns

def show_url_partterns(urlpartterns):
    """
        @description: show all urlpartterns
    """
    print_title("Websocket urlpartterns")
    for urlparttern in urlpartterns:
        print_title ((urlparttern))