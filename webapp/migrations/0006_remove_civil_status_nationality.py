# Generated by Django 4.1.2 on 2022-10-17 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_civil_status_nationality_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='civil_status',
            name='nationality',
        ),
    ]
