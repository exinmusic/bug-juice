from django.db import models
from django.contrib.auth.models import User


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
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    report_type = models.CharField(max_length=16, choices=TYPE_CHOICES, default='bug')
    department = models.CharField(max_length=16, choices=DEPARTMENT_CHOICES, default='back')
    error_log = models.TextField(max_length=600, default="")
    note = models.TextField(max_length=600, default="")
    bug = models.BooleanField(default=False)
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    approved_comment = models.BooleanField(default=False)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.created_date)