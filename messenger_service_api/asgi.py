# messenger_service_api/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# from channels.layers import get_channel_layer
# from channels_redis.core import RedisChannelLayer


# Asegúrate de que las configuraciones de Django se establezcan antes de importar otros módulos
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messenger_service_api.settings')
application = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import user_chat.routing  # Importa el enrutador de tu aplicación

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            user_chat.routing.websocket_urlpatterns  # Usa el enrutador de tu aplicación
        )
    ),
})


# # Configuración del ProtocolTypeRouter para incluir CHANNEL_LAYERS
# application = ProtocolTypeRouter({
#     "websocket": RedisChannelLayer(
#         # Esta línea se agrega para que Django pueda trabajar con canales
#         "django.core.asgi.channels_layers",
#         "default",
#     ),
# })