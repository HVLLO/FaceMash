import json

from django.test import TestCase, Client
from django.urls import reverse

from api.account.models import User


# TODO: This class must test API for CRUD Post
class TestAPIPost(TestCase):
    def setUp(self):
        self.c = Client()
        usr, is_created = User.objects.get_or_create(username='NewUser',
                                                     email='NewUser@gmail.com')

        if is_created:
            usr.set_password('Password')
            usr.save()

        self.client.login(email='NewUser@gmail.com', password='Password')
        self.valid_post = {
            'author': usr,
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

    # def test_when_user_was_update_profile(self):
    #     data = {
    #         'email': 'NewUser@gmail.com',
    #         'password': 'Password',
    #     }
    #     jwt_response = self.client.post(reverse('obtain_jwt'), data=data)
    #     self.assertEqual(jwt_response.status_code, status.HTTP_200_OK)
    #
    #     token = json.loads(jwt_response.content.decode('utf-8'))['access']
    #     response = self.client.post(reverse('update_user'), Authorization=f'Bearer: {token}',
    #                                 data=data, format='json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)