from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models

@login_required
def report(request, rid):
    return render(request, "reports/report.html", {"rid":rid})
