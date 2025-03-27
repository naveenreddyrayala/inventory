from django.urls import path
from . import views
urlpatterns = [
    path('todos/', views.todos, name='Todos'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("<int:id>", views.index, name="index"),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
]