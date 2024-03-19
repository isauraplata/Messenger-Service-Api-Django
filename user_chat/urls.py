# # user_chat/urls.py Rutas de la aplicación
from django.urls import path, re_path
from .views import home, chat_messages
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    re_path(r'^messages/$', chat_messages, name='chat_messages'),
]

