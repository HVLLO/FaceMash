from django.test import TestCase, Client

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
        self.c = Client
