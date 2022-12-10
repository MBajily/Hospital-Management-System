# Generated by Django 4.1.2 on 2022-12-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0048_alter_hospitalprofile_user_alter_patientprofile_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="hospitalprofile",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="patientprofile",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="stuff",
            name="id",
            field=models.IntegerField(
                default=39460976755, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
