# Generated by Django 4.1.2 on 2022-10-30 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_kin_email_alter_hospital_hospital_id_alter_stuff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hospital_id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='id',
            field=models.IntegerField(default=61110398762, editable=False, primary_key=True, serialize=False),
        ),
    ]
