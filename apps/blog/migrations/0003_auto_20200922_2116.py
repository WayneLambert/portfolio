# Generated by Django 3.1.1 on 2020-09-22 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200921_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'default_manager_name': 'objects', 'ordering': ['-updated_date', '-publish_date']},
        ),
    ]
