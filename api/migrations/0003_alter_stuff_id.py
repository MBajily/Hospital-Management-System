# Generated by Django 4.1.2 on 2022-10-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_medical_examination_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]