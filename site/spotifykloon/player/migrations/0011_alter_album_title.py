# Generated by Django 4.2.5 on 2023-09-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("player", "0010_alter_album_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
