# Generated by Django 4.2.6 on 2023-10-17 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking", old_name="first_name", new_name="name",
        ),
        migrations.RenameField(model_name="menu", old_name="name", new_name="title",),
    ]
