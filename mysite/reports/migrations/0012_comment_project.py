# Generated by Django 2.2.6 on 2020-01-17 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_auto_20200117_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reports.Project'),
        ),
    ]