# Generated by Django 4.2.4 on 2023-08-08 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruds', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
