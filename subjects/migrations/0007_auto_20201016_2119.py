# Generated by Django 3.1.2 on 2020-10-16 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0006_auto_20201016_1649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['created_on']},
        ),
    ]
