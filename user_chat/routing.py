# user_chat/routing.py Rutas de Websockets 

# from django.urls import path
# from .consumers import ChatConsumer

# websocket_urlpatterns = [
#     path('ws/messages/', ChatConsumer.as_asgi()),
# ]

# # Se especifica la ruta de los websockets (ws/chat/) y se conecta a un consumidor, que es responsable de manejar la lógica de la conexión websocket.se define las rutas para los websockets de tu aplicación


# user_chat/routing.py Enrutamiento de WebSocket
from django.urls import re_path
from .consumers import ChatConsumer


websocket_urlpatterns = [
    # re_path(r'ws/messages/$', ChatConsumer.as_asgi()),
    re_path(r'ws/messages/$', ChatConsumer.as_asgi()),
]
