# Generated by Django 4.2.5 on 2023-10-06 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("player", "0005_opiniononsong_opinion"),
    ]

    operations = [
        migrations.AddField(
            model_name="opiniononsong",
            name="artist",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="player.artist",
            ),
        ),
    ]
