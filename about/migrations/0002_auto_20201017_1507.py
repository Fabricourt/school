# Generated by Django 3.1.2 on 2020-10-17 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['date_posted'], 'verbose_name': 'Team', 'verbose_name_plural': 'Triza Academy Team'},
        ),
    ]