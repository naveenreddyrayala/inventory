from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import TodoItem, ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'myapp/list.html', {"ls":ls})

def home(response):
    return render(response, 'myapp/home.html', {})

def create(response):
    form = CreateNewList()
    return render(response, 'myapp/create.html', {"form": form})