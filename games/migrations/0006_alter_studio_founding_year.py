# Generated by Django 4.2.4 on 2023-08-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_rename_developer_game_studio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='founding_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
