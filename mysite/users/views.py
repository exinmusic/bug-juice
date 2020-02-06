from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from . import models
from reports.models import Project
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

# LOGOUT
@login_required
def logout(request):
    logout_user(request)
    return redirect("/users/login")

# USER PROFILE
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

# SIGNUP
def signup(request):
    return render(request, "users/signup.html")

# CREATE NEW USER+PROJECT
def create(request):
    # POST
    if request.method == "POST":
        # If existing project.
        if not Project.objects.filter(name=request.POST.get('project')):
            # Create New Project
            p = Project.objects.create(
                        name = request.POST.get('project')
                        )
            # Create New User in Project
            u = models.User.objects.create_user( request.POST.get('username'), request.POST.get('email'), request.POST.get('password') )
            u.profile.project = p
            u.save()
            return redirect("/users/login")
    # GET
    else:
        return render(request, "users/create_project.html")

# JOIN EXISTING PROJECT w/ NEW USER
def join(request):
    # POST
    if request.method == "POST":
        p = Project.objects.get(name=request.POST.get('project'))
        # If Project exists
        if p:
            u = models.User.objects.create_user( request.POST.get('username'), request.POST.get('email'), request.POST.get('password') )
            u.profile.project = p
            u.save()

            return redirect("/users/login")
    # GET
    else:
        return render(request, "users/join_project.html")