# Generated by Django 3.1.1 on 2020-09-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]