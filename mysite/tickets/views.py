from django.shortcuts import render
from django.http import HttpResponse
from . import models
from datetime import datetime

def tickets(request):
    reports = models.Report.objects.all().values()
    return render(request, "tickets/tickets.html", {"reports":reports})

def submit(request):
    if request.method == "POST":
        report_data = {}
        report_data['nickname'] = request.POST.get('nickname')
        report_data['report_type'] = request.POST.get('report_type')
        report_data['department'] = request.POST.get('department')
        report_data['description'] = request.POST.get('description')
        report_data['reporter'] = 'default_dev'
        print(report_data)
        return render(request, "tickets/submit.html")
    else:
        return render(request, "tickets/submit.html")