# Generated by Django 4.2.5 on 2023-09-11 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("player", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Music",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="MusicTrack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField()),
                ("file", models.FileField(upload_to="static/music/")),
                (
                    "music",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="player.music"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="MusicTrackModel",
        ),
    ]