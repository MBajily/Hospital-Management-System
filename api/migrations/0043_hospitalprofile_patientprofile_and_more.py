# Generated by Django 4.1.2 on 2022-12-04 05:25

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0042_alter_stuff_id_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="HospitalProfile",
            fields=[
                (
                    "hospital_id",
                    models.IntegerField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("logo", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="PatientProfile",
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
                ("phone", models.CharField(max_length=20)),
                (
                    "civil_status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.civil_status",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="patient",
            name="civil_status",
        ),
        migrations.RemoveField(
            model_name="basic_health_state",
            name="hospital",
        ),
        migrations.RemoveField(
            model_name="basic_health_state",
            name="patient",
        ),
        migrations.RemoveField(
            model_name="kin",
            name="patient",
        ),
        migrations.RemoveField(
            model_name="medical_examination",
            name="hospital",
        ),
        migrations.RemoveField(
            model_name="medical_examination",
            name="patient",
        ),
        migrations.RemoveField(
            model_name="prescription",
            name="hospital",
        ),
        migrations.RemoveField(
            model_name="prescription",
            name="patient",
        ),
        migrations.RemoveField(
            model_name="stuff",
            name="hospital",
        ),
        migrations.AlterField(
            model_name="stuff",
            name="id",
            field=models.IntegerField(
                default=16644771489, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.DeleteModel(
            name="Hospital",
        ),
        migrations.DeleteModel(
            name="Patient",
        ),
        migrations.CreateModel(
            name="Hospital",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("api.user",),
            managers=[
                ("hospital", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("api.user",),
            managers=[
                ("patient", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="patientprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="api.patient"
            ),
        ),
        migrations.AddField(
            model_name="hospitalprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="api.hospital"
            ),
        ),
    ]
