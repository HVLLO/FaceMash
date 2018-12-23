from django.test import TestCase, Client

from api.account.models import User


# TODO: This class must test API for CRUD User model
class TestAPIUser(TestCase):
    def setUp(self):
        self.c = Client()

    def test_user_create_profile(self):
        pass


