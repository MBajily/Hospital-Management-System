# Generated by Django 4.1.2 on 2022-11-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_remove_basic_health_state_result_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_health_state',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='id',
            field=models.IntegerField(default=49261820172, editable=False, primary_key=True, serialize=False),
        ),
    ]
