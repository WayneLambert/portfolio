# Generated by Django 3.0.8 on 2020-07-26 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countdown_numbers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_nums',
            field=models.CharField(max_length=255),
        ),
    ]
