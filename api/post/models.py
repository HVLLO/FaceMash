from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from root.settings import AUTH_USER_MODEL
from api.like.models import Like


class Post(models.Model):
    """
    Create a model Post, we associate it with the Like model through GenericRelation:
    """
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_user')
    title = models.CharField(max_length=99)
    body = models.TextField(max_length=500)
    publish_date = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like)

    @property
    def publish(self):
        return self.publish_date

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
