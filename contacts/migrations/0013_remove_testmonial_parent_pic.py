# Generated by Django 3.1.2 on 2020-10-18 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_auto_20201018_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmonial',
            name='parent_pic',
        ),
    ]
