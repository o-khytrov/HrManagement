# Generated by Django 5.0.7 on 2024-07-14 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('position', models.CharField(max_length=128)),
                ('date_of_hire', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to='employees.employee')),
            ],
        ),
    ]
