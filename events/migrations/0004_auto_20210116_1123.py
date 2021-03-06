# Generated by Django 3.1.5 on 2021-01-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210116_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(blank=True, help_text='Ending time of the event.', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(blank=True, help_text='Starting time of the event.', null=True),
        ),
    ]
