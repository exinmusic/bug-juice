# Generated by Django 2.2.6 on 2020-01-15 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20200109_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='bug',
            new_name='confirmed',
        ),
    ]
