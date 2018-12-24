import json

from django.test import Client
from django.urls import reverse
from django.test.client import RequestFactory

from rest_framework import status
from rest_framework.test import APITestCase

from api.account.models import User
from api.like.models import Like
from .REST_API.serializers import PostSerializer
from .models import Post


class TestAPIPost(APITestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()

        usr, is_created = User.objects.get_or_create(username='NewUser',
                                                     email='NewUser@gmail.com')
        if is_created:
            usr.set_password('Password')
            usr.save()

        self.client.login(email='NewUser@gmail.com', password='Password')

        # Create JWT token for auth
        data = {
            'email': 'NewUser@gmail.com',
            'password': 'Password',
        }
        jwt_response = self.client.post(reverse('obtain_jwt'), data=data)
        self.token = json.loads(jwt_response.content.decode('utf-8'))['access']

        # Create Post
        Post.objects.create(author=usr, title='First Post Title', body='First Post Body')
        Post.objects.create(author=usr, title='Lorem ', body='ipsum')
        Post.objects.create(author=usr, title='Apple', body='A12 best mobile processor')
        Post.objects.create(author=usr, title='Intel', body='Core i9 last processor from company')
        Post.objects.create(author=usr, title='Sony',
                            body='Playstation 4 Pro -> best platform for gaming in upscale 4k')

    def test_when_user_create_post(self):
        """
        User create new post:
        prepare data:               -> author(who), title, body
        serializer data
        send POST request with data and JWT auth token
        check http status 201 to create.
        """

        author = User.objects.get(email='NewUser@gmail.com')
        valid_post = {
            'author': author,
            'title': 'Title One',
            'body': 'Body One',
        }

        serializer = PostSerializer(valid_post)
        response = self.client.post(reverse('post_router-list'), Authorization=f'Bearer: {self.token}',
                                    data=serializer.data, format='json')
        post = Post.objects.filter(author=author, title='Title One', body='Body One')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(post.exists())

    def test_when_user_want_update_post_info(self):
        """
        User update post information:
        prepare data:                   -> author(who), new title, new body
        serializer data
        send PATCH request with data and JWT auth token
        check status and check new response data
        """

        author = User.objects.get(email='NewUser@gmail.com')
        post = Post.objects.get(title='First Post Title', body='First Post Body')

        update_post = {
            'author': author,
            'title': 'Update Title One',
            'body': 'Update Body One',
        }
        serializer = PostSerializer(update_post)
        response = self.client.patch(reverse('post_router-detail', kwargs={'pk': post.pk}),
                                     Authorization=f'Bearer: {self.token}',
                                     data=serializer.data, format='json')
        patch_post = Post.objects.get(pk=post.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(post.title, patch_post.title)
        self.assertEqual(patch_post.title, update_post['title'])
        self.assertEqual(patch_post.body, update_post['body'])

    def test_when_user_want_liked_post(self):
        """
        User liked post:
        get user and post record                    -> user.pk, post.pk
        send POST request with post data and JWT auth token
        check status and check liked post
        """

        author = User.objects.get(email='NewUser@gmail.com')
        post = Post.objects.get(title='Lorem ', body='ipsum')

        response = self.client.post(reverse('post_router-like', kwargs={'pk': post.pk}),
                                    Authorization=f'Bearer: {self.token}',
                                    format='json')
        like = Like.objects.get(user=author)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(like.user, author)
        self.assertEqual(like.content_object, post)

    def test_when_user_want_unlike_post(self):
        """
        User liked post:
        get post record                    -> post.pk
        send POST request with post data and JWT auth token
        check status and check for missing record
        """

        post = Post.objects.get(title='Lorem ', body='ipsum')

        response = self.client.post(reverse('post_router-unlike', kwargs={'pk': post.pk}),
                                    Authorization=f'Bearer: {self.token}',
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertRaises(Like.DoesNotExist, Like.objects.get)

    def test_when_user_want_see_who_liked_post(self):
        """
        User is viewing everyone who likes the post
        get post record                    -> post.pk
        send GET request with post data and JWT token
        check status code
        """

        post = Post.objects.get(title='Lorem ', body='ipsum')
        response = self.client.get(reverse('post_router-fans', kwargs={'pk': post.pk}),
                                   Authorization=f'Bearer: {self.token}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_viewing_post(self):
        """
        User is viewing everyone posts
        get post record                    -> post.pk
        send GET request with post data and JWT token
        check status code and check response data
        """

        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)
        response = self.client.get(reverse('post_router-list'), Authorization=f'Bearer: {self.token}', )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_user_viewing_detail_post(self):
        """
        User is viewing one posts
        get post record                    -> post.pk
        send GET request with post data and JWT token
        check status code and check response data
        """

        post = Post.objects.get(title='Lorem ', body='ipsum')
        serializer = PostSerializer(post)

        response = self.client.get(reverse('post_router-detail', kwargs={'pk': post.pk}),
                                   Authorization=f'Bearer: {self.token}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
