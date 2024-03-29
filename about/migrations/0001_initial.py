# Generated by Django 3.1.2 on 2020-10-17 11:22

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='about', max_length=200, null=True, unique=True)),
                ('statement', models.CharField(max_length=400)),
                ('description', ckeditor.fields.RichTextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
                ('image', models.ImageField(null=True, upload_to='About/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
                'ordering': ['date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('title', models.CharField(max_length=400)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_mvp', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('image', models.ImageField(null=True, upload_to='Team/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Lapset Ajibika Team',
                'ordering': ['date_posted'],
            },
        ),
    ]
