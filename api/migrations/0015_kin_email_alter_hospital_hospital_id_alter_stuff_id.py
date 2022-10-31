# Generated by Django 4.1.2 on 2022-10-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_hospital_username_alter_hospital_hospital_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kin',
            name='email',
            field=models.EmailField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_id',
            field=models.IntegerField(default=56353301443, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='id',
            field=models.IntegerField(default=64873568692, editable=False, primary_key=True, serialize=False),
        ),
    ]
