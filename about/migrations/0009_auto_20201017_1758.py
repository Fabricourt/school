# Generated by Django 3.1.2 on 2020-10-17 14:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_auto_20201017_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='aboutteam',
            field=ckeditor.fields.RichTextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='welcome_message',
            field=ckeditor.fields.RichTextField(max_length=300, null=True),
        ),
    ]
