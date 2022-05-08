from cProfile import run
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from virtualenv import session_via_cli
from .models import *
import pygame
from subprocess import PIPE, run
from django.contrib import messages

# Create your views here.
def index(request):
    # print(request.GET)
    
    id = request.session['id']
    #request.GET['userid']
    # print(queryID)
    user = Users.objects.get(id=id)
    # print(user)
    context = {
        "id":user.id,
        "User": user,
        "favorite_color": "red",
        "pets": ["tonail", "gabe", "Sir Squash"],
        "FirstName": user.firstName
    }
    return render(request, "index.html", context)

        #return HttpResponse("this is the equivalent of @app.routes('/')")
        

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")


def attemptLogin(request):
    if request.method == "POST":
        formEmail = request.POST['email']
        formPassword = request.POST['password']
        user = Users.objects.get(email=formEmail)
        # if bcrypt.checkpw(request.POST['passwordlogin'].encode(), 
        #     logged_user.password.encode())

        print("-------------------------------")
        print(user)
        print("-------------------------------")

        if(user == None):
            print("Login failed")
            return render(request, "login.html")
        print (user.id)
        request.session['id'] = user.id
        return redirect("/login")

    return redirect("/")

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
        user = Users.objects.create(email = formEmail, password = formPassword, confirmpass = formConfirmpass, firstName = formFirstName, lastName = formLastName)
        print(user)
        request.session['id'] = user.id
        return redirect("/login")

def gamepage (request):
    return render(request,"gamepage.html")

def playgame (request):
    return render(request, "rungame.html")


def my_game(request):
    command = ['sudo', 'python test_data.py']
    result = run(command, stdout=PIPE, stderr=PIPE, shell=True, universal_newlines=True)
    return render(request, 'mygame.py',{'data1':result})

def highscores(request):
    id = request.session['id']#request.GET['userid']
    # gamesList = Games.objects.all()
    # gamesList.
    # for game in gameList:
    scoresList = Scores.objects.all()#.filter(games_id=id)
    print(scoresList)
    scoresViewModelDict = {}
    for score in scoresList:
        gameName = score.games_id.name
        scoreVm = ScoresViewModel()
        scoreVm.gameName = gameName
        scoreVm.userName = score.users_id.firstName
        scoreVm.score = score.score
        scoreVm.timestamp = score.timestamp
        scoresViewModelDict.setdefault(gameName, []).append(scoreVm)
    for key, value in scoresViewModelDict.items():
        print(key, value)
    #print(scoresViewModelDict)
    return render(request, "highscores.html", {'Model': scoresViewModelDict })

def grabScore(request):
    if(request.method == "GET"):
        return render(request, "rungame.html")
    if(request.method == "POST"):
        return highscores(request)


def addFavorite(request):
    favgame = []
    if (request.method == "GET"):
        return render(request, "gamepage")
    if (request.method == "POST"):
        return Games.name.append.favgame(request, "index", favgame)
    