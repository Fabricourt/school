# Generated by Django 3.1.2 on 2020-10-17 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_slide_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='is_footer_1',
        ),
        migrations.RemoveField(
            model_name='page',
            name='is_footer_2',
        ),
        migrations.RemoveField(
            model_name='page',
            name='is_footer_3',
        ),
    ]
