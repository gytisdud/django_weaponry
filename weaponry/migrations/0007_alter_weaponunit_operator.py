# Generated by Django 4.1.5 on 2023-01-30 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weaponry', '0006_alter_weaponunit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weaponunit',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='weaponry.soldier'),
        ),
    ]
