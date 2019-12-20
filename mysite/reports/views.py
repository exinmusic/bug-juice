from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models

@login_required
def report(request, rid):
    # CURRENT REPORT
    r = models.Report.objects.get(id=rid)

    # POST
    if request.method == "POST":
        models.Comment.objects.create(
            author = request.user,
            text = request.POST.get('text'),
            report = r
        )
        return render(request, "reports/report.html", {"report":r})
    # GET
    else:
        return render(request, "reports/report.html", {"report":r})


