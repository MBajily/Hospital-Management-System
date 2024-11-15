# Generated by Django 4.1.2 on 2022-10-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Civil_Status',
            fields=[
                ('nationality_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200, null=True)),
                ('birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male - ذكر'), ('Female', 'Female - أنثى')], max_length=200, null=True)),
                ('nationality', models.CharField(choices=[('Sudanese', 'Sudanese - سوداني'), ('Non-sudanese', 'Non-sudanese - غير سوداني')], max_length=200, null=True)),
            ],
        ),
    ]
