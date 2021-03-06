# Generated by Django 2.2.6 on 2019-12-06 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=600)),
                ('time_reported', models.DateTimeField(auto_now_add=True)),
                ('reporter', models.CharField(max_length=80)),
                ('report_type', models.CharField(choices=[('Bug', 'Bug'), ('Vulnerability', 'Vulnerability'), ('Feature request', 'Feature Request')], default='bug', max_length=16)),
                ('department', models.CharField(choices=[('Database', 'Database'), ('User Auth', 'User Auth'), ('Styling', 'Styling'), ('Front-end', 'Front-end'), ('Back-end', 'Back-end')], default='back', max_length=16)),
                ('error_log', models.TextField(default='', max_length=600)),
                ('note', models.TextField(default='', max_length=600)),
                ('bug', models.BooleanField(default=False)),
                ('solved', models.BooleanField(default=False)),
            ],
        ),
    ]
