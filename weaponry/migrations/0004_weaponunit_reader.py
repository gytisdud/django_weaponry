# Generated by Django 4.1.5 on 2023-01-29 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weaponry', '0003_weapon_cover_alter_soldier_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='weaponunit',
            name='reader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
