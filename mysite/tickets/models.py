from django.db import models

class Report(models.Model):
    nickname = models.CharField(max_length=25)
    description = models.TextField(max_length=600)
    time_reported = models.DateTimeField()
    reporter = models.CharField(max_length=80)
    