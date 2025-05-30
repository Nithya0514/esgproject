# Generated by Django 5.2.1 on 2025-05-30 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esgapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_units', to='esgapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('environmental', 'Environmental'), ('social', 'Social'), ('governance', 'Governance')], max_length=20)),
                ('year', models.PositiveIntegerField()),
                ('value', models.FloatField()),
                ('business_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metrics', to='esgapp.businessunit')),
            ],
        ),
    ]
