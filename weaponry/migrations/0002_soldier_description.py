# Generated by Django 4.1.5 on 2023-01-29 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weaponry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldier',
            name='description',
            field=models.TextField(default='', max_length=2000, verbose_name='Aprašymas'),
        ),
    ]
