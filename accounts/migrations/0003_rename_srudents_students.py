# Generated by Django 5.1.3 on 2024-12-10 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_srudents"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Srudents",
            new_name="Students",
        ),
    ]