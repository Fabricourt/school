# Generated by Django 3.1.2 on 2020-10-09 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_auto_20201008_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='students',
        ),
    ]
