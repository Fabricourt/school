# Generated by Django 3.1.2 on 2020-10-17 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='description',
        ),
    ]
