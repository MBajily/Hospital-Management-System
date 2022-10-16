# Generated by Django 4.1.2 on 2022-10-16 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('nationality_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.civil_status')),
            ],
        ),
        migrations.CreateModel(
            name='Kin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('relationship', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Husband', 'Husband'), ('Wife', 'Wife'), ('Son', 'Son'), ('Daughter', 'Dauther'), ('Brother', 'Father'), ('Sister', 'Sister'), ('Uncle', 'Uncle'), ('aunt', 'aunt'), ('Grandfather', 'Grandfather'), ('grandmother', 'grandmother'), ('Step Father', 'Step Father'), ('Step Mother', 'Step Mother')], max_length=200)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.patient')),
            ],
        ),
    ]
