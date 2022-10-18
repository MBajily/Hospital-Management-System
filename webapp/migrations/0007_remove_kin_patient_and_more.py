# Generated by Django 4.1.2 on 2022-10-18 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_remove_civil_status_nationality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kin',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='medical_examination',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='medical_examination',
            name='stuff',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='nationality_id',
        ),
        migrations.RemoveField(
            model_name='stuff',
            name='hospital',
        ),
        migrations.DeleteModel(
            name='Civil_Status',
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
        migrations.DeleteModel(
            name='Kin',
        ),
        migrations.DeleteModel(
            name='Medical_Examination',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Stuff',
        ),
    ]
