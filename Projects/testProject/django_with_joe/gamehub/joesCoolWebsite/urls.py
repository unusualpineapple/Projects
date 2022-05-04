from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('logout',views.logout),
    path('', views.index),
    path('register', views.register),
    path('create_user', views.create_user),
    path('highscores', views.highscores),
    path('gamepage', views.gamepage),
    path('playgame', views.playgame),
]