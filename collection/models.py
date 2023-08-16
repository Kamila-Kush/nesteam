from django.contrib.auth.models import User
from django.db import models
from games.models import Game
# Create your models here.

class GameCollection(models.Model):
    name = models.CharField(max_length=100)
    games_list = models.ManyToManyField(
        to=Game,
        blank=True,
        related_name='game_collection'
    )
    author = models.ForeignKey(
        to=User,
        related_name='game_collection',
        verbose_name='автор',
        on_delete=models.PROTECT,
        null=True
    )
    likes = models.ManyToManyField(
        to=User,
        blank=True,
        related_name='liked_collection'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']