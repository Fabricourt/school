# Generated by Django 3.1.2 on 2020-10-18 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0001_initial'),
        ('contacts', '0011_address_phone_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmonial',
            name='parent_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='myparent', to='parents.parent'),
        ),
    ]
