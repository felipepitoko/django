from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def todo(request):
    items = TodoItem.objects.all() #pega todos os itens do banco de dados
    return render(request, "todos.html", {"todos": items})
