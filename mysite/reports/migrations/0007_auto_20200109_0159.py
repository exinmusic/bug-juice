# Generated by Django 2.2.6 on 2020-01-09 01:59

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20191220_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='department',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Database', 'Database'), ('User Auth', 'User Auth'), ('Styling', 'Styling'), ('Front-end', 'Front-end'), ('Back-end', 'Back-end')], default='Back-end', max_length=5),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Feature request', 'Feature Request')], default='Bug', max_length=16),
        ),
    ]