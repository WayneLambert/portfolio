# Generated by Django 3.2.5 on 2021-08-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtoken',
            name='challenge_completed_timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]