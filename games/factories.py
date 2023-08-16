import factory
from .models import Game, Genre, Studio

class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre
    name = factory.Sequence(
        lambda n: f'Test genre_{n}'
    )
    description = 'Test description'

class StudioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Studio
    name = factory.Sequence(
        lambda n: f'Test studio_{n}'
    )

class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    name = factory.Sequence(
        lambda n: f'Test game_{n}'
    )
    year = factory.Sequence(
        lambda y: y
    )
    genre = factory.SubFactory(GenreFactory)