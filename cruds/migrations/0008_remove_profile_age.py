# Generated by Django 4.2.4 on 2023-08-09 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruds', '0007_remove_profile_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
    ]
