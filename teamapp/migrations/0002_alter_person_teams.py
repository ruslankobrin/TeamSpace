# Generated by Django 5.0.1 on 2024-01-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teamapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="teams",
            field=models.ManyToManyField(
                blank=True, related_name="members", to="teamapp.team"
            ),
        ),
    ]
