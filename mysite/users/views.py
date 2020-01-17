from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from . import models
from itertools import chain

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
            return redirect("/dashboard")
        else:
            # Return an 'invalid login' error message.
            return render(request, "users/login.html")
    # GET
    else:
        if request.GET.get('next'):
            return render(request, "users/login_required.html")
        else:
            return render(request, "users/login.html")

@login_required
def logout(request):
    logout_user(request)
    return redirect("/users/login")

def signup(request):
    return render(request, "users/signup.html")

@login_required
def profile(request):


    comments = request.user.comment_set.all()
    reports = request.user.report_set.all()
    feed = sorted(
        chain(comments,reports),
        key = lambda instance: instance.created_date,
        reverse=True
    )

    return render(request, "users/profile.html", {"feed":feed})