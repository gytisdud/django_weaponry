# Generated by Django 4.1.5 on 2023-01-31 13:09

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('weaponry', '0012_alter_weaponunit_due_back_alter_weaponunit_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldier',
            name='assigned_weapons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='weaponry.weaponunit'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='weaponunit',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Assigned'), ('n', 'Not assigned')], default='n', help_text='Status', max_length=1),
        ),
    ]
