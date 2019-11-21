from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from . import models

# LOGIN
def login(request):
    # POST
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username)
        if user is not None:
            login_user(request, user)
            return redirect("/tickets")
        else:
            # Return an 'invalid login' error message.
            return render(request, "users/login.html")
    # GET
    else:
        return render(request, "users/login.html")

def logout(request):
    logout_user(request)
    return redirect("/users/login")