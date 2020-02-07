from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from reports import models
from itertools import chain

# HOME
def home(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    else:
        return render(request, "tickets/home.html")

# SUBMIT TICKET
@login_required
def submit(request):
    # POST
    if request.method == "POST":
        models.Project.objects.get(id=request.user.profile.project.id).report_set.create(name=request.POST.get('name'),
									report_type=request.POST.get('report_type'),
									department=request.POST.getlist('department'),
									description=request.POST.get('description'),
                                    author=request.user,
                                    error_log=request.POST.get('error_log'),
                                    note=request.POST.get('note'))                          
        return redirect("/dashboard/tickets")
    # GET
    else:
        return render(request, "tickets/submit.html")

# DASHBOARD
@login_required
def dash(request):
    project = models.Project.objects.get(id=request.user.profile.project.id)
    reports = project.report_set.filter(confirmed=False,solved=False)
    bugs = project.report_set.filter(confirmed=True,solved=False,report_type='Bug')
    features = project.report_set.filter(confirmed=True,solved=False,report_type='Feature')
    solutions = project.report_set.filter(solved=True)
    comments = project.comment_set.all()
    feed = sorted(
        chain(reports,bugs,features,solutions,comments),
        key = lambda instance: instance.created_date,
        reverse=True
    )
    return render(request, "tickets/dash.html", {"reports":reports, "bugs":bugs, "features":features, "solutions":solutions, "feed":feed})

# TICKETS VIEW
@login_required
def tickets(request):
    project = models.Project.objects.get(id=request.user.profile.project.id)
    reports = project.report_set.filter(confirmed=False,solved=False)
    bugs = project.report_set.filter(confirmed=True,solved=False,report_type='Bug')
    features = project.report_set.filter(confirmed=True,solved=False,report_type='Feature')

    return render(request, "tickets/tickets.html", {"reports":reports, "bugs":bugs, "features":features})

# SOLUTIONS VIEW
@login_required
def solutions(request):
    project = models.Project.objects.get(id=request.user.profile.project.id)
    solutions = project.report_set.filter(solved=True)
    return render(request, "tickets/tickets.html", {"solutions":solutions})

def permission_denied_view(request, exception):
    return render(request, "tickets/error.html", {"exception":exception,"code":403})

def not_found_view(request, exception):
    return render(request, "tickets/error.html", {"exception":exception,"code":404})