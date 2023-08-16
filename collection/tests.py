from rest_framework.test import APITestCase

from games.models import Studio, Genre
from .factories import CollectionFactory
from .models import *


class CollectionsTest(APITestCase):
    def setUp(self):
        self.col_1 = CollectionFactory()
        self.col_2 = CollectionFactory()
        self.col_3 = CollectionFactory()


    def test_get_list_of_3_collections(self):
        response = self.client.get('/collections/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.col_1.name, response.data[0]["name"])
        self.assertEqual(self.col_2.name, response.data[1]["name"])
        self.assertEqual(self.col_3.name, response.data[2]["name"])

    def test_get_one_collection(self):
        response = self.client.get(f'/collections/{self.col_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.col_1.name, response.data["name"])

    def test_post_new_collection(self):
# можно ли в сетапе прописать фактори другой модели, чтобы ее можно было положить в пост запрос?

        data = {
            'name': 'test_collection',
        }
        response = self.client.post('/collections/', data)
        self.assertEqual(response.status_code, 201)

        collection = GameCollection.objects.last()
        self.assertEqual(collection.name, response.data["name"])
        self.assertEqual(GameCollection.objects.count(), 4)


    def test_put_collection(self):
        data = {
            'name': 'test_collection_update',
        }
        response = self.client.put(f'/collections/{self.col_1.pk}/', data)

        self.assertEqual(response.status_code, 200)
        test_collection_update = GameCollection.objects.get(pk=self.col_1.pk)
        self.assertEqual(test_collection_update.name, data['name'])

    def test_delete_collection(self):
        response = self.client.delete(f'/collections/{self.col_1.pk}/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(GameCollection.objects.filter(pk=self.col_1.pk).exists())
