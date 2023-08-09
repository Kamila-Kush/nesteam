from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)

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
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Игра'
        verbose_name_plural='Игры'