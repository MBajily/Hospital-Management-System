# Generated by Django 4.1.2 on 2022-11-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_rename_note_medical_examination_report_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='id',
            field=models.IntegerField(default=66676064418, editable=False, primary_key=True, serialize=False),
        ),
    ]