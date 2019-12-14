# Generated by Django 2.2.6 on 2019-12-14 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='reporter',
        ),
        migrations.AddField(
            model_name='report',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
