# # user_chat/consumers.py
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from .models import Message
# from django.contrib.auth import get_user_model

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = 'chat'
#         self.room_group_name = f'chat_{self.room_name}'

#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         print(data)
#         user = self.scope['user']
#         message_content = data['message']
#         print(message_content)

#         # Usa una lista en memoria para almacenar los mensajes
#         Message.in_memory_messages.append({'author': user.username, 'content': message_content})
#         await self.send_messages()

#     async def send_messages(self):
#         messages = Message.in_memory_messages
#         await self.send(text_data=json.dumps({'messages': messages}))

# user_chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from django.contrib.auth import get_user_model

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'chat'
        self.room_group_name = f'chat_{self.room_name}'

        # aqui me uni
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # aqui me salgo yo
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        user = self.scope['user']
        message_content = data['message']
        print(message_content)

        # se guarda el mensaje en la lista en memoria, pq no usamos bd aun xd
        Message.in_memory_messages.append({'author': user.username, 'content': message_content})

        # aqui se envia mensajes a todos los participantes del grupo
        await self.send_messages()

    async def send_messages(self):
        # Obtener todos los mensajes de la lista en memoria
        messages = Message.in_memory_messages

        # Enviar mensajes al grupo
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'messages': messages
            }
        )

    async def chat_message(self, event):
        # Enviar el mensaje al cliente que solicitó el mensaje
        messages = event['messages']
        await self.send(text_data=json.dumps({'messages': messages}))
