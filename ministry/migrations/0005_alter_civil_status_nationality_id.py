# Generated by Django 4.1.2 on 2022-10-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0004_medical_examination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civil_status',
            name='nationality_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]