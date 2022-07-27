# create user
from os import access
import django.contrib.auth.models
from .models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


def create_user(username, first_name, last_name, email, password):
    newUser = User(username = username, first_name = first_name, last_name = last_name, email = email, password = password)
    newUser.is_superuser = True;
    newUser.is_staff = True;
    newUser.save()
    return newUser

# delete owner accout 
def delete_account(username):
    # delete the parent user model instance
    user_instance = User.objects.get(username = username)
    user_instance.delete()
    
def request_login(request, username, password):
    access = authenticate(request, username = username, password = password)
    
    if access is not None:
        login(request, access)
        return {"status": 200, "details": "user logged in", "auth":True}
    else:
        return {"status": 400, "details": "login failed", "auth":False}
    
def user_logout(request):
    logout(request)