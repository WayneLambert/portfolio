# Generated by Django 3.2.6 on 2021-08-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_challenge_token_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtoken',
            name='challenge_completed_timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]