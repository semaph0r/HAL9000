# Generated by Django 2.1.15 on 2020-12-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20201208_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='expired_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]