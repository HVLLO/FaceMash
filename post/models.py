from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from root.settings import AUTH_USER_MODEL


# This model refer to the generic type of model
class Like(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='user_like',
                             blank=True, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    objects_id = models.PositiveIntegerField()
    content_objects = GenericForeignKey('content_type', 'objects_id')


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
