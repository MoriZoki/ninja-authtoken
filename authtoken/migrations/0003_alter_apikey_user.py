# Generated by Django 5.0.7 on 2024-07-14 12:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0002_remove_apikey_expires_at_remove_apikey_revoked'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='key', to=settings.AUTH_USER_MODEL),
        ),
    ]