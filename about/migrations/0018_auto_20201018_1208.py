# Generated by Django 3.1.2 on 2020-10-18 09:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0017_auto_20201018_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='welcome_message',
            field=ckeditor.fields.RichTextField(max_length=600, null=True),
        ),
    ]
