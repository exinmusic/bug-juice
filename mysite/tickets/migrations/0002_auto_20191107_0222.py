# Generated by Django 2.2.6 on 2019-11-07 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='bug',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='time_reported',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]