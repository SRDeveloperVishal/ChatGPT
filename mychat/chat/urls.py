from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_room, name='chat_room'),
    path('chat/', views.chat_room_two, name='chat_room_two'),
]
