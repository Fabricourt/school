# Generated by Django 3.1.2 on 2020-10-20 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_student_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='parent',
            new_name='contact_parent',
        ),
    ]