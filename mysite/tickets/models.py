from django.db import models

TYPE_CHOICES = (
	("bug","Bug"),
    ("vulnerability","Vulnerability"),
	("feature request","Feature Request"),
)

DEPARTMENT_CHOICES = (
    ("db","Database"),
    ("auth","User Auth"),
    ("styling","Styling"),
    ("front","Front-end App"),
    ("back","Back-end App"),
)

class Report(models.Model):
    nickname = models.CharField(max_length=25)
    description = models.TextField(max_length=600)
    time_reported = models.DateTimeField()
    reporter = models.CharField(max_length=80)
    report_type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='bug')
    department = models.CharField(max_length=6, choices=DEPARTMENT_CHOICES, default='back')

    def __str__(self):
        return self.nickname