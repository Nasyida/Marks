# Generated by Django 3.1.7 on 2021-04-24 18:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory_page', '0030_auto_20210415_2311'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='enter',
            new_name='enter_marks',
        ),
    ]
