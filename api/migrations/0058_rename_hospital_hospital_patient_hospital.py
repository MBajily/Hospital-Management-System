# Generated by Django 4.1.2 on 2023-01-08 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0057_delete_stuff"),
    ]

    operations = [
        migrations.RenameField(
            model_name="hospital_patient",
            old_name="Hospital",
            new_name="hospital",
        ),
    ]