from django.db import models

TYPE_CHOICES = (
	("Bug","Bug"),
    ("Vulnerability","Vulnerability"),
	("Feature request","Feature Request"),
)

DEPARTMENT_CHOICES = (
    ("Database","Database"),
    ("User Auth","User Auth"),
    ("Styling","Styling"),
    ("Front-end","Front-end"),
    ("Back-end","Back-end"),
)

class Report(models.Model):
    nickname = models.CharField(max_length=25)
    description = models.TextField(max_length=600)
    time_reported = models.DateTimeField(auto_now_add=True, blank=True)
    reporter = models.CharField(max_length=80)
    report_type = models.CharField(max_length=16, choices=TYPE_CHOICES, default='bug')
    department = models.CharField(max_length=16, choices=DEPARTMENT_CHOICES, default='back')
    error_log = models.TextField(max_length=600, default="")
    note = models.TextField(max_length=600, default="")
    bug = models.BooleanField(default=False)
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname

class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)