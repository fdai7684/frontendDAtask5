# Generated by Django 4.2 on 2023-05-09 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footballapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubs',
            name='seasonticketholders',
        ),
    ]
