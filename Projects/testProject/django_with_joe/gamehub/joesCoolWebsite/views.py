from cProfile import run
from distutils.log import error
from unicodedata import name
import bcrypt
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from virtualenv import session_via_cli
from .models import *
import pygame
from subprocess import PIPE, run
from django.contrib import messages


# Create your views here.
def index(request):
    userlog = Users.objects.filter(id = request.session['id'])
    userlog2 = Users.objects.get(id = request.session['id'])
    print(userlog2.favoritedgames.all())

    usergames = Games.objects.first()
    print(usergames.usersthatfav.all())

    context = {
        'user' : userlog[0],
        'games' : Games.objects.all(),
        # 'favgame': Games.usersthatfav.objects.all()
        'favgame' : userlog2.favoritedgames.all()
    }
    return render(request, "index.html", context)

def validateLogin(request):
    user = Users.get.objects.get(email=request.POST['email'])
    if bcrypt.checkpw(request.POST['passwordlogin'].encode(), user.password.encode()):
        print("password match")
    else:
        print("failed password")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")


def attemptLogin(request):

    user = Users.objects.filter(email=request.POST['email'])
    if user:
        loggedin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),loggedin.password.encode()):
            request.session['id'] = loggedin.id
            return redirect('/login')
    return redirect('/')



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

def gamepage (request):
    if 'id' not in request.session:
        return redirect("/login")
    # # request.session['id']
    return render(request,"gamepage.html", {'games' : Games.objects.all()})

def playgame (request, game_id):
    userlog = Users.objects.filter(id = request.session['id'])
    # print 
    context = {
        'this_game_id' : Games.objects.get(id = game_id),
        'all' : Scores.objects.all(),
        'user' : userlog[0],
    }
    # {request.session['id']: Users.objects.get(name = firstName)
    return render (request, "rungame.html", context)


# def my_game(request):
#     command = ['sudo', 'python test_data.py']
#     result = run(command, stdout=PIPE, stderr=PIPE, shell=True, universal_newlines=True)
#     return render(request, 'mygame.py',{'data1':result})

# def grabGame(request):
#     games = Games.objects.all()

def highscores(request):
    scoresList = Scores.objects.all()#.filter(games_id=id)
    print(scoresList)
    scoresViewModelDict = {}
    for score in scoresList:
        gameName = score.games_id.name
        scoreVm = ScoresViewModel()
        scoreVm.gameName = gameName
        scoreVm.userName = score.users_id.firstName
        scoreVm.score = score.scores
        scoreVm.timestamp = score.timestamp
        scoresViewModelDict.setdefault(gameName, []).append(scoreVm)
    for key, value in scoresViewModelDict.items():
        print(key, value)
        

    return render(request, "highscores.html", {'Model': scoresViewModelDict })

def grabScore(request):
    if(request.method == "GET"):
        return render(request, "rungame.html")
    if(request.method == "POST"):
        return highscores(request)


def addFavorite(request, game_id):
    user = Users.objects.get(id = request.session['id'])
    game = Games.objects.get(id = game_id)
    user.favoritedgames.add(game)
    return redirect('/login')


def subscore(request):
    if(request.method == "GET"):
        return render(request, "rungame.html")
    if (request.method == "POST"):
        return render ("highscores.html", Scores)
    

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

def deleteFavorite(request, game_id):
    user = Users.objects.get(id = request.session['id'])
    game = Games.objects.get(id = game_id)
    user.favoritedgames.remove(game)
    return redirect('/login')