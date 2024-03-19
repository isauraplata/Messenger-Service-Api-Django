# # user_chat/models.py
# from django.db import models
# from django.contrib.auth.models import User

# class Message(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)



# user_chat/models.py
# user_chat/models.py
# user_chat/models.py

# from django.db import models
# from django.contrib.auth import get_user_model

# class Message(models.Model):
#     author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     # Otros campos de tu modelo

#     def save(self, *args, **kwargs):
#         from .consumers import ChatConsumer  # Importa aquí para evitar la importación circular
#         if not self.author_id:
#             User = get_user_model()
#             user_instance = User.objects.get(username="nombre_de_prueba")
#             self.author = user_instance
#         super().save(*args, **kwargs)





# # user_chat/models.py
# from django.db import models
# from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .consumers import ChatConsumer

# class Message(models.Model):
#     author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     content = models.TextField()

# @receiver(post_save, sender=Message)
# def save_message(sender, instance, **kwargs):
#     if not instance.author_id:
#         User = get_user_model()
#         user_instance = User.objects.get(username="nombre_de_prueba")
#         instance.author = user_instance
#     ChatConsumer.send_messages()  # Llamar a la función para enviar mensajes después de guardar







# user_chat/models.py
from django.db import models
from django.contrib.auth import get_user_model

class Message(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(default='') 
    
Message.in_memory_messages = []

