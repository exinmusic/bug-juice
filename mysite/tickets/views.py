from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from reports import models
from itertools import chain

# HOME
def home(request):
    return render(request, "tickets/home.html")

# SUBMIT TICKET
@login_required
def submit(request):
    # POST
    if request.method == "POST":
        report_data = {}
        report_data['name'] = request.POST.get('name')
        report_data['report_type'] = request.POST.get('report_type')
        report_data['department'] = request.POST.get('department')
        report_data['description'] = request.POST.get('description')
        report_data['author'] = request.user
        report_data['error_log'] = request.POST.get('error_log')
        report_data['note'] = request.POST.get('note')
        models.Report.objects.create(name=report_data['name'],
									report_type=report_data['report_type'],
									department=report_data['department'],
									description=report_data['description'],
                                    author=report_data['author'],
                                    error_log=report_data['error_log'],
                                    note=report_data['note'])
        all_reports = models.Report.objects.filter(bug=False)                            
        return render(request, "tickets/tickets.html", {"reports":all_reports})
    # GET
    else:
        return render(request, "tickets/submit.html")

def dash(request):
    reports = models.Report.objects.filter(bug=False)
    bugs = models.Report.objects.filter(bug=True)
    solutions = models.Report.objects.filter(solved=True)
    comments = models.Comment.objects.all()
    feed = sorted(
        chain(reports,bugs,solutions,comments),
        key = lambda instance: instance.created_date,
        reverse=True
    )
    return render(request, "tickets/dash.html", {"reports":reports, "bugs":bugs, "features":0, "solutions":solutions, "feed":feed})

# MANAGE TICKETS
@login_required
def tickets(request):

    # POST
    if request.method == "POST":
        manage_req = request.POST.get('manage')
        report_id = request.POST.get('report_id')
        print("Ticket management...")

        # USERS SELECTS bug
        if manage_req == "bug":
            try:
                entry = models.Report.objects.get(id=report_id)
                entry.bug = True
                entry.save()
                reports = models.Report.objects.filter(bug=False)
                bugs = models.Report.objects.filter(bug=True)
                return render(request, "tickets/tickets.html", {"reports":reports, "bugs":bugs})
            except:
                print('No report by that ID found...')

        # USERS SELECTS review
        if manage_req == "review":
            return redirect("reports/"+report_id)

    # GET
    else:
        reports = models.Report.objects.filter(bug=False)
        bugs = models.Report.objects.filter(bug=True)
        solutions = models.Report.objects.filter(solved=True)
        comments = models.Comment.objects.all()
        feed = sorted(
            chain(reports,bugs,solutions,comments),
            key = lambda instance: instance.created_date,
            reverse=True
        )

        return render(request, "tickets/tickets.html", {"reports":reports, "bugs":bugs, "features":0, "solutions":solutions, "feed":feed})

# SOLVE BUGS
@login_required
def bugs(request):
    all_bugs = models.Report.objects.all().filter(bug=True, solved=False).values()
    return render(request, "tickets/bugs.html", {"bugs":all_bugs})

# VIEW SOLUTIONS
@login_required
def solutions(request):
    all_solutions = models.Report.objects.all().filter(solved=True).values()
    return render(request, "tickets/solutions.html", {"solutions":all_solutions})