# Generated by Django 3.1.2 on 2020-10-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colors', '0002_auto_20201010_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='color_pics'),
        ),
    ]
