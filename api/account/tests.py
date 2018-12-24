from django.test import Client
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class TestAPIUser(APITestCase):
    def setUp(self):
        self.c = Client()

    def test_user_create_profile(self):
        data = {
            'username': 'user',
            'email': 'email@gmail.com',
            'password': 'Password',
            'first_name': 'First',
            'last_name': 'Last',
        }
        response = self.client.post(reverse('create_user'), data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(email=data['email']).email, 'email@gmail.com')
