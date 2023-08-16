import factory
from .models import GameCollection
from usersapp.factories import UserFactory



class CollectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GameCollection

    name = factory.Sequence(
        lambda number: f'Test collection_{number}'
    )
    author = factory.SubFactory(UserFactory)