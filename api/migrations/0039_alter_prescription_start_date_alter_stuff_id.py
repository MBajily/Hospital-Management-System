# Generated by Django 4.1.2 on 2022-11-11 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_prescription_note_alter_stuff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='start_date',
            field=models.DateField(default=datetime.date(2022, 11, 11)),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='id',
            field=models.IntegerField(default=87059546993, editable=False, primary_key=True, serialize=False),
        ),
    ]
