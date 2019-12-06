from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models

@login_required
def report(request, rid):
    r = models.Report.objects.all().filter(id=rid).values()
    return render(request, "reports/report.html", {"report":r[0]})
