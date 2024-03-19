from django.contrib import admin

# Register your models here.
from .models import Message
# from .models import Chat, Message

# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('user', 'chat', 'message', 'timestamp')
#     list_filter = ('chat', 'user')

# admin.site.register(Message, MessageAdmin)
admin.site.register(Message)