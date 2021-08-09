# Generated by Django 3.2.5 on 2021-08-05 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_challenge_completed_timestamp_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailtoken',
            name='challenge_token_returned',
        ),
        migrations.AlterField(
            model_name='emailtoken',
            name='challenge_completed_timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]