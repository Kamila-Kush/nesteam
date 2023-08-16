# Generated by Django 4.2.4 on 2023-08-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_studio_game_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(default='Нет описания'),
        ),
        migrations.AlterField(
            model_name='game',
            name='developer',
            field=models.ManyToManyField(blank=True, to='games.studio', verbose_name='Разработчики'),
        ),
    ]