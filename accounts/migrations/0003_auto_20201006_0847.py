# Generated by Django 3.0.6 on 2020-10-06 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201006_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_headgir',
            new_name='is_headgirl',
        ),
    ]