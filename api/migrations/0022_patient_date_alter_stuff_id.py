# Generated by Django 4.1.2 on 2022-11-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_stuff_id_patient_medical_examination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='id',
            field=models.IntegerField(default=46053049545, editable=False, primary_key=True, serialize=False),
        ),
    ]
