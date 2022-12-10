# Generated by Django 4.1.2 on 2022-12-04 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0043_hospitalprofile_patientprofile_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="basic_health_state",
            name="patient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="basic_health_state_patient",
                to="api.patient",
            ),
        ),
        migrations.AddField(
            model_name="kin",
            name="patient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="kin_patient",
                to="api.patient",
            ),
        ),
        migrations.AddField(
            model_name="medical_examination",
            name="patient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="medical_examination_patient",
                to="api.patient",
            ),
        ),
        migrations.AddField(
            model_name="prescription",
            name="patient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="patient",
                to="api.patient",
            ),
        ),
        migrations.AddField(
            model_name="stuff",
            name="hospital",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="stuff_hospital",
                to="api.hospital",
            ),
        ),
        migrations.AlterField(
            model_name="stuff",
            name="id",
            field=models.IntegerField(
                default=18147581681, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
