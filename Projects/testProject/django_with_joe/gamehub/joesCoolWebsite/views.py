from cProfile import run
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
import pygame
from subprocess import PIPE, run

# Create your views here.

def index(request):
    # print(request.GET)

    id = request.session['id']#request.GET['userid']
    # print(queryID)

    user = Users.objects.get(id=id)
    # print(user)
    context = {
        "User": user,
        "favorite_color": "red",
        "pets": ["tonail", "gabe", "Sir Squash"],
        "FirstName": user.firstName
    }
    return render(request, "index.html", context)
    #return HttpResponse("this is the equivalent of @app.routes('/')")

def register(request):
    return render(request, "register.html")

def highscores(request):

    
    id = request.session['id']#request.GET['userid']

    # gamesList = Games.objects.all()
    # gamesList.
    # for game in gameList:

    scoresList = Scores.objects.all()#.filter(games_id=id)
    print(scoresList)
    return render(request, "highscores.html", {'data': scoresList })

def login(request):
    if(request.method == "GET"):
        return render(request, "login.html")
    if(request.method == "POST"):
        return attemptLogin(request)

def attemptLogin(request):
    formEmail = request.POST['email']
    formPassword = request.POST['password']

    user = Users.objects.filter(email=formEmail, password=formPassword).first()

    if(user == None):
        print("Login failed")
        return render(request, "login.html")

    request.session['id'] = user.id
    
    return redirect("/")
    

def create_user(request):
    print("Get POST info")
    print(request.POST)

    formEmail = request.POST['email']
    formPassword = request.POST['password']
    formFirstName = request.POST['firstName']
    formLastName = request.POST['lastName']

    user = Users.objects.create(email = formEmail, password = formPassword, firstName = formFirstName, lastName = formLastName)

    print(user)

    request.session['id'] = user.id

    return redirect("/")

def gamepage (request):
    return render(request,"gamepage.html")

def playgame (request):
    return render(request, "rungame.html")


def my_game(request):
    command = ['sudo', 'python test_data.py']
    result = run(command, stdout=PIPE, stderr=PIPE, shell=True, universal_newlines=True)
    return render(request, 'mygame.py',{'data1':result})

# def grabscore(request):


#try AJAX from html page 
