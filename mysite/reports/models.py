from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


TYPE_CHOICES = (
	("Bug","Bug"),
	("Feature","Feature"),
)

DEPARTMENT_CHOICES = (
    ("Database","Database"),
    ("User Auth","User Auth"),
    ("Styling","Styling"),
    ("Front-end","Front-end"),
    ("Back-end","Back-end"),
)

class Report(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=600)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    report_type = models.CharField(max_length=16, choices=TYPE_CHOICES, default='Bug')
    department = MultiSelectField(max_length=100, choices=DEPARTMENT_CHOICES, default='Back-end')
    error_log = models.TextField(max_length=600, default="")
    note = models.TextField(max_length=600, default="")
    confirmed = models.BooleanField(default=False)
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    approved_comment = models.BooleanField(default=False)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.created_date)

class Todo(models.Model):
    name = models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name