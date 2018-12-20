from django.test import TestCase, Client

from rest_framework.test import APIRequestFactory

from account.models import User
from post.models import Post, Like


# TODO: This class must test API for CRUD User model
class TestAPIUser(TestCase):
    def setUp(self):
        self.c = Client()

    @staticmethod
    def test_user_create_profile(self):
        pass


# TODO: This class must test API for CRUD Post
class TestAPIPost(TestCase):
    def setUp(self):
        user = User.objects.get_or_create(username='johnlennon',
                                          email='johnlennon@gmail.com,', password='qwerty12345')

        self.c = Client
        self.valid_post = {
            'author': user,
            'title': 'Title One',
            'body': 'Body One',
        }
        self.invalid_post = {
            'author': None,
            'title': 'Title One',
            'body': 'Body One',
        }

    def test_when_user_create_post(self):
        pass
