from django.urls import path
from . import views

urlpatterns = [
    path('login', views.index),
    path('logout',views.logout),
    path('', views.login),
    path('attemptlogin', views.attemptLogin),
    path('register', views.register),
    path('create_user', views.create_user),
    path('highscores', views.highscores),
    path('gamepage', views.gamepage),
    path('playgame', views.playgame),
]