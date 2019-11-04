from django.shortcuts import render
from django.http import HttpResponse
from . import models

def tickets(request):
    reports = models.Report.objects.all().values()
    return render(request, "tickets/tickets.html", {"reports":reports})

def submit(request):
    return render(request, "tickets/submit.html")