# Generated by Django 3.1.2 on 2020-10-10 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notice_board', '0002_auto_20201008_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='class_name',
        ),
        migrations.AddField(
            model_name='notice',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='notice_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
