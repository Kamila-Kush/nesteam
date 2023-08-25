from django.contrib.auth.models import User
from rest_framework.test import APITestCase


from .models import *

class UserTest(APITestCase):
    def create_new_user_by_APIView(self):
        #RegistrationAPIView
        data = {
            'username': 'test_user',
            'password': 'test_password123'
        }
        response = self.client.post('/users/registration/', data)
        self.assertEqual(response.status_code, 201)

        new_user = User.objects.last()
        self.assertEqual(new_user.username, response.data["username"])
        self.assertEqual(new_user.password, response.data["password"])
        self.assertEqual(new_user.id, response.data["id"])

    def create_new_user_by_djoser(self):
        #djoser
        data = {
            'username': 'test_user',
            'password': 'test_password123'
        }
