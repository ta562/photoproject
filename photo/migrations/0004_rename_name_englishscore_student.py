# Generated by Django 5.1.3 on 2024-12-10 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("photo", "0003_remove_englishscore_user_englishscore_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="englishscore",
            old_name="name",
            new_name="student",
        ),
    ]
