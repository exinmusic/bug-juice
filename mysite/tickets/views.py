from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    reports = models.Report.objects.all().values()
    return render(request, "tickets/index.html", {"reports":reports})