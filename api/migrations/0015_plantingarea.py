# Generated by Django 3.1.5 on 2021-02-10 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210203_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantingArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('accuracy', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('planting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.planting')),
            ],
        ),
    ]
