# Generated by Django 3.1.2 on 2020-10-17 15:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_auto_20201017_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='aboutteam',
        ),
        migrations.AddField(
            model_name='about',
            name='aboutourleaders',
            field=ckeditor.fields.RichTextField(max_length=500, null=True),
        ),
    ]
