from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models

@login_required
def report(request, rid):
    # CURRENT REPORT
    r = models.Report.objects.get(id=rid)
    return render(request, "reports/report.html", {"report":r})

@login_required
def manage(request, rid):
    # POST
    if request.method == "POST":
        manage_req = request.POST.get('selection')
        report_id = rid
        print("Ticket management...")

        # USERS SELECTS Confirm
        if manage_req == "Confirm":
            try:
                entry = models.Report.objects.get(id=report_id)
                entry.confirmed = True
                entry.save()
                return redirect('/dashboard/tickets')
            except:
                print('No report by that ID found...')

        # USERS SELECTS Review
        if manage_req == "Review":
            return redirect("/reports/"+report_id)

        # USERS SELECTS Close
        if manage_req == "Close":
            return redirect("/reports/"+report_id)

        # USERS SELECTS Solve
        if manage_req == "Solve":
            return redirect("/reports/"+report_id)

@login_required
def comment(request, rid):
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

        