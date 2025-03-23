from django.contrib import admin
from myapp.models import TodoItem, ToDoList, Item
# Register your models here.

admin.site.register(TodoItem)
admin.site.register(ToDoList)
admin.site .register(Item)