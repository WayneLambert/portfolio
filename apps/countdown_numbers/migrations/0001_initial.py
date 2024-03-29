# Generated by Django 3.1.1 on 2020-09-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NumbersGame",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("game_nums", models.CharField(max_length=255)),
                ("target_number", models.IntegerField()),
                ("player_num_achieved", models.IntegerField()),
                ("valid_calc", models.BooleanField(default=False)),
                ("comp_num_achieved", models.IntegerField()),
                ("player_score", models.IntegerField(default=0)),
                ("comp_score", models.IntegerField(default=0)),
                ("solution_str", models.CharField(max_length=255)),
                ("game_result", models.CharField(max_length=255)),
                ("entry_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ("-entry_date",),
            },
        ),
    ]
