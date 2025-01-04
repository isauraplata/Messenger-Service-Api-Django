# user_chat/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.core.cache import cache
from datetime import datetime

class Message(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Lista en memoria para los mensajes
    in_memory_messages = []

    @staticmethod
    def get_messages_from_cache():
        messages = cache.get('chat_messages', [])
        return messages

    @staticmethod
    def save_message_to_cache(message_dict):
        messages = Message.get_messages_from_cache()
        messages.append(message_dict)
        cache.set('chat_messages', messages)
        return messages

    
    
    