from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('thread/create_thread/', views.CreateThreadView),
    path('<str:link>', views.BoardView)
]
