# Generated by Django 3.1.2 on 2020-10-23 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teacher_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='class_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='school_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
