from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import TodoItem, ToDoList, Item

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def index(request, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br><p>%s</>p" %(ls.name, str(item.text)))

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")