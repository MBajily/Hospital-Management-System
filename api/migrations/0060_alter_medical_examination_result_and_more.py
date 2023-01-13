# Generated by Django 4.1.2 on 2023-01-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0059_alter_hospitalprofile_user_alter_patientprofile_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medical_examination",
            name="result",
            field=models.FileField(
                upload_to="C:\\Users\\mbaji\\Desktop\\Django\\Seha\\static/media"
            ),
        ),
        migrations.AlterField(
            model_name="medical_examination",
            name="type",
            field=models.CharField(
                choices=[
                    ("Biopsy", "Biopsy"),
                    ("Colonoscopy", "Colonoscopy"),
                    ("CT scan", "CT scan"),
                    ("Electrocardiogram (ECG)", "Electrocardiogram (ECG)"),
                    ("Electroencephalogram (EEG)", "Electroencephalogram (EEG)"),
                    ("Gastroscopy", "Gastroscopy"),
                    ("Eye tests", "Eye tests"),
                    ("Hearing test", "Hearing test"),
                    ("MRI scan", "MRI scan"),
                    ("PET scan", "PET scan"),
                    ("Ultrasound", "Ultrasound"),
                    ("X-rays", "X-rays"),
                ],
                max_length=200,
            ),
        ),
    ]