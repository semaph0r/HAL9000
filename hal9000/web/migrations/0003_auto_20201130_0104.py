# Generated by Django 3.1.3 on 2020-11-30 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20201130_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='acknowledged_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='notified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
