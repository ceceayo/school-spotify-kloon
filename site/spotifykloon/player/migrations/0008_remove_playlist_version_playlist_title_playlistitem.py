# Generated by Django 4.2.6 on 2023-10-13 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("player", "0007_playlist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="playlist",
            name="version",
        ),
        migrations.AddField(
            model_name="playlist",
            name="title",
            field=models.CharField(
                default="OwO anime body pillow licking addiction *nuzzles you*",
                max_length=100,
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="PlaylistItem",
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
                (
                    "pl",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="player.playlist",
                    ),
                ),
                (
                    "version",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="player.musictrack",
                    ),
                ),
            ],
        ),
    ]