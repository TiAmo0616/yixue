from django.urls import re_path

from app01 import consumers,canvasconsumer
#re_path(r'(?P<username>\w+)/room(?P<group>\w+)/$', consumers.ChatConsumer.as_asgi()),
websocket_urlpatterns = [re_path(r'(?P<username>\w+)/canvas(?P<group>\w+)/$', canvasconsumer.ChatConsumer1.as_asgi()),
                         re_path(r'(?P<username>\w+)/room(?P<group>\w+)/$', consumers.ChatConsumer.as_asgi())]

