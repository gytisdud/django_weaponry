# Generated by Django 4.1.5 on 2023-01-31 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weaponry', '0014_remove_soldier_assigned_weapons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weaponunit',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Assigned'), ('n', 'Not assigned')], default='a', help_text='Status', max_length=1),
        ),
    ]
