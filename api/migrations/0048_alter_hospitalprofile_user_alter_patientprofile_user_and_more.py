# Generated by Django 4.1.2 on 2022-12-06 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0047_alter_stuff_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hospitalprofile",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.hospital"
            ),
        ),
        migrations.AlterField(
            model_name="patientprofile",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.patient"
            ),
        ),
        migrations.AlterField(
            model_name="stuff",
            name="id",
            field=models.IntegerField(
                default=34444689593, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
