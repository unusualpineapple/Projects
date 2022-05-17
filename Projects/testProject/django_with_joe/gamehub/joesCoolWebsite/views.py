from cProfile import run
from distutils.log import error
from multiprocessing import context
from unicodedata import name
from xml.etree.ElementTree import Comment
import bcrypt
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from virtualenv import session_via_cli
from .models import *
import pygame
from subprocess import PIPE, run
from django.contrib import messages



def login(request):
    return render(request, "login.html")

def attemptLogin(request):
    errors = Users.objects.loginval(request.POST)
    # errors = Users.logs.loginval(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    # if user:
    user = Users.objects.get(email = request.POST['email'])
    loggedin = user
    #     if bcrypt.checkpw(request.POST['password'].encode(),loggedin.password.encode()):
    #         return redirect('/login')
    request.session['id'] = loggedin.id
    return redirect('/login')

def logout(request):
    del request.session['id']
    return redirect('/')

def create_user(request):
    print("Get POST info")
    print(request.POST)
    errors = Users.objects.validation(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/register')
    else:
        formEmail = request.POST['email']
        formPassword = request.POST['password']
        formConfirmpass = request.POST['confirmpass']
        formFirstName = request.POST['firstName']
        formLastName = request.POST['lastName']
        pwhash = bcrypt.hashpw(formPassword.encode(), bcrypt.gensalt()).decode()
        createduser = Users.objects.create(email = formEmail, password = pwhash, firstName = formFirstName, lastName = formLastName)

        request.session['id'] = createduser.id
        return redirect("/login")

# Create your views here.
def register(request):
    return render(request, "register.html")

def index(request):
    userlog2 = Users.objects.get(id = request.session['id'])
    print(userlog2.favoritedgames.all())
    usergames = Games.objects.first()
    print(usergames.usersthatfav.all())
    context = {
        'user' : userlog2,
        'games' : Games.objects.all(),
        # 'gamenames': Games.objects.get(name ='gamenames'),
        'favgame' : userlog2.favoritedgames.all(),
        'comments': Comments.objects.all()
    }
    return render(request, "index.html", context)

def gamepage (request):
    if 'id' not in request.session:
        return redirect("/login")
    userlog2 = Users.objects.get(id = request.session['id'])
    context = {
        # 'faves' : Users.favoritedgames.filter(),
        'comments': Comments.objects.all(),
        'games' : Games.objects.all(),
        'user': userlog2,
        'favgames': []
    }
    return render(request,"gamepage.html", context)

def playgame (request, game_id):
    userlog2 = Users.objects.get(id = request.session['id'])
    # print 
    context = {
        'this_game_id' : Games.objects.get(id = game_id),
        'all' : Scores.objects.all(),
        'user' : userlog2,
        'comments':Comments.objects.all()
    }
    # {request.session['id']: Users.objects.get(name = firstName)
    return render (request, "rungame.html", context)

def insertscore(request):
    formgames_id = int(request.POST['games_id'])
    formusers_id = request.session['id']
    formScore = int(request.POST['score'])
    getgame = Games.objects.get(id = formgames_id)
    getuser = Users.objects.get(id = formusers_id)
    if (formScore == ""):
        return redirect('/rungame/<int:game_id>')
    Scores.objects.create(games_id = getgame, users_id = getuser, scores = formScore)
    return redirect('/highscores')

def grabScore(request):
    if(request.method == "GET"):
        return render(request, "rungame.html")
    if(request.method == "POST"):
        return highscores(request)

def subscore(request):
    if(request.method == "GET"):
        return render(request, "rungame.html")
    if (request.method == "POST"):
        return render ("highscores.html", Scores)
    
def highscores(request):
    userlog2 = Users.objects.get(id = request.session['id'])
    scoresList = Scores.objects.all().order_by('-scores')
    listofgames = Games.objects.all()
    print(scoresList)
    #sudo coding
    #i want to loop through all the games
    scoresViewModelDict = {}
    for game in listofgames:
        #listofgames length
        # scoresViewModelDict[i] = arr[game]
        gamescorelist = scoresList.filter(games_id = game.id)[:10]
        for score in gamescorelist:
            gameName = score.games_id.name
            scoreVm = ScoresViewModel()
            scoreVm.gameName = gameName
            scoreVm.userName = score.users_id.firstName
            scoreVm.score = score.scores
            scoreVm.timestamp = score.timestamp
            scoresViewModelDict.setdefault(gameName, []).append(scoreVm)
        #pull the game out one by one
        # return gamescorelist
    #I want to filter the score list to a single game and limit the resilts to 5
    for key, value in scoresViewModelDict.items():
        print(key, value)
    context = {
        'user' : userlog2,
        'Model': scoresViewModelDict
    }
    return render(request, "highscores.html", context)
    #add to those 5 scores to the viewmodelDict
    #return the viewmodeldict

def addFavorite(request, game_id):
    user = Users.objects.get(id = request.session['id'])
    game = Games.objects.get(id = game_id)
    user.save()
    user.favoritedgames.add(game)
    return redirect('/login')

def deleteFavorite(request, game_id):
    user = Users.objects.get(id = request.session['id'])
    game = Games.objects.get(id = game_id)
    user.favoritedgames.remove(game)
    return redirect('/login')

def addComment(request):
    errors = Comments.objects.validation(request.POST)
    # errors = Users.logs.loginval(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/login')
    user = Users.objects.get(id = request.session['id'])
    game = Games.objects.get(id = request.POST['games_id'])
    newuserComment = Comments.objects.create(comment=request.POST['comment'], games_id =game, users_id= user )
    user.usercomments.add(newuserComment)
    return redirect('/login')


def deleteComment(request, comment_id):
    user = Users.objects.get(id = request.session['id'])
    comment = Comments.objects.get(id = comment_id)
    # user.usercomments.delete(comment)
    comment.delete()
    return redirect('/login')

def updateComment(request, comment_id):
    user = Users.objects.get(id = request.session['id'])
    updateComment = Comments.objects.get(id = comment_id)
    updateComment.comment = request.POST['comment']
    updateComment.save()
    return redirect("/login")



