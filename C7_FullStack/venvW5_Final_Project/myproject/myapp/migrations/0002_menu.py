# Generated by Django 4.2.6 on 2023-10-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.CharField(max_length=200)),
                ("price", models.IntegerField()),
                (
                    "menu_item_description",
                    models.TextField(default="", max_length=1000),
                ),
            ],
        ),
    ]
