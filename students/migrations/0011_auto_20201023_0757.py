# Generated by Django 3.1.2 on 2020-10-23 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20201020_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='school_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
