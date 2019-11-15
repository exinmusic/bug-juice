from django.shortcuts import render
from django.http import HttpResponse
from . import models

# LOGIN
def login(request):
    return render(request, "users/login.html")