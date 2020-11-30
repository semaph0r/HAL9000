# Generated by Django 3.1.3 on 2020-11-30 01:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='acknowledged_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='acknowledged_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='certificate_acknowledge_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='domain',
            field=models.TextField(null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='maintainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='certificate_maintainer_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='notified_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='software',
            name='acknowledged_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='software',
            name='acknowledged_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='software_acknowledge_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='software',
            name='maintainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='software_maintainer_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='software',
            name='notified_at',
            field=models.DateTimeField(null=True),
        ),
    ]
