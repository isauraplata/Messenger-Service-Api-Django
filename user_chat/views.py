from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Message

def home(request):
    if request.user.is_authenticated:
        return redirect('chat_messages')  # Renombrado para evitar conflictos
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat_messages')  # Renombrado para evitar conflictos
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'chat/home.html', {'form': form})


def chat_messages(request):  # Renombrado para evitar conflictos
    all_messages = Message.objects.all()
    return render(request, 'chat/messages.html', {'messages': all_messages})
