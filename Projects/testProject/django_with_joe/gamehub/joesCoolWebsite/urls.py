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
    path('playgame/<int:game_id>', views.playgame),
    path('insertscore', views.insertscore),
    path('addfavgame/<int:game_id>',views.addFavorite),
    path('deletefavgame/<int:game_id>', views.deleteFavorite),
    path('adduserComment', views.addComment),
    path('deleteComment/<int:comment_id>', views.deleteComment),
    path('updatecomment/<int:comment_id>', views.updateComment)
]