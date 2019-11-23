from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models

# SUBMIT TICKET
@login_required
def submit(request):
    # POST
    if request.method == "POST":
        report_data = {}
        report_data['nickname'] = request.POST.get('nickname')
        report_data['report_type'] = request.POST.get('report_type')
        report_data['department'] = request.POST.get('department')
        report_data['description'] = request.POST.get('description')
        report_data['reporter'] = request.user.username
        report_data['error_log'] = request.POST.get('error_log')
        report_data['note'] = request.POST.get('note')
        models.Report.objects.create(nickname=report_data['nickname'],
									report_type=report_data['report_type'],
									department=report_data['department'],
									description=report_data['description'],
                                    reporter=report_data['reporter'],
                                    error_log=report_data['error_log'],
                                    note=report_data['note'])
        all_reports = models.Report.objects.all().filter(bug=False).values()                            
        return render(request, "tickets/tickets.html", {"reports":all_reports})
    # GET
    else:
        return render(request, "tickets/submit.html")

# MANAGE TICKETS
@login_required
def tickets(request):
    # POST
    if request.method == "POST":
        manage_req = request.POST.get('manage')
        report_id = request.POST.get('report_id')
        print("Ticket management...")
        if manage_req == "bug":
            try:
                entry = models.Report.objects.get(id=report_id)
                entry.bug = True
                entry.save()
            except:
                print('No report by that ID found...')

            all_reports = models.Report.objects.all().filter(bug=False).values()
            return render(request, "tickets/tickets.html", {"reports":all_reports})
    # GET
    else:
        all_reports = models.Report.objects.all().filter(bug=False).values()
        return render(request, "tickets/tickets.html", {"reports":all_reports})

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

# REVIEW REPORT
@login_required
def review(request):
    return render(request, "tickets/review.html")