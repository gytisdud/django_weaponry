# Generated by Django 4.1.5 on 2023-01-31 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weaponry', '0011_delete_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weaponunit',
            name='due_back',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='weaponunit',
            name='status',
            field=models.CharField(blank=True, choices=[('t', 'Assigned'), ('a', 'Not assigned')], default='na', help_text='Status', max_length=1),
        ),
    ]
