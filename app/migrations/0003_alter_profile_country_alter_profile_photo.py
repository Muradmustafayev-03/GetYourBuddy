# Generated by Django 4.0.1 on 2022-01-26 21:14

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_profile_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
