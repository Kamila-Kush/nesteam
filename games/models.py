from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='Нет описания')

    def __str__(self):
        return self.name

class Studio(models.Model):
    name = models.CharField(max_length=255)
    workers_count = models.PositiveIntegerField(null=True, blank=True)
    games_count = models.PositiveIntegerField()
    founding_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=255, )
    year = models.PositiveIntegerField()
    genre = models.ForeignKey(
        to='Genre',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='жанр'
    )
    developer = models.ManyToManyField(
        to=Studio,
        blank=True,
        verbose_name='Разработчики'
    )


    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'



