# Generated by Django 3.1.2 on 2020-10-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0005_auto_20201016_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='unmarked',
            field=models.BooleanField(blank=True, default=True, help_text='do not click on this unless advised otherwise', null=True),
        ),
    ]
