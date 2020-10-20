# Generated by Django 3.1.2 on 2020-10-16 17:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('is_mvp', models.BooleanField(default=False)),
                ('account_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parent_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
