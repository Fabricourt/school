# Generated by Django 3.1.2 on 2020-10-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20201017_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='title1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title3',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
