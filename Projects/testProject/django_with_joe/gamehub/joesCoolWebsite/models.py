from django.db import models
import re
class Userval(models.Manager):
    def validation(self, postData):
        errors = {}
        REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['firstName']) <5 :
            errors['firstName'] = "must have a valid name"
        if len(postData['lastName']) <5 : 
            errors['lastName'] = "lets try again for that last name"
        if len(postData['password']) <3 :
            errors['password'] = "come on thats all you want for a password make it longer"
        if (postData['confirmpass']) == postData['password']:
            errors['confirmpass'] = "you didnt type the same password lets try again"
        if not REGEX.match(postData['email']):
            errors['email'] = "invalid email bub"
        return errors
# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    firstName = models.CharField(max_length=225)
    lastName = models.CharField(max_length=225)
    createdat = models.DateTimeField(auto_now_add=True)
    updateddat = models.DateTimeField(auto_now=True)
    objects = Userval()


class Games(models.Model):
    name = models.CharField(max_length=225)
    createdat = models.DateTimeField(auto_now_add=True)
    updateddat = models.DateTimeField(auto_now=True)

class Scores(models.Model):
    games_id = models.ForeignKey(Games, on_delete=models.CASCADE, related_name = 'gamescores')
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='userscores')
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)

class ScoresViewModel():
    gameName: str
    userName: str
    score: int
    timestamp: str