from django.db import models

from root.settings import AUTH_USER_MODEL


class Post(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_user')
    title = models.CharField(max_length=99)
    body = models.TextField(max_length=500)
    publish_date = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(AUTH_USER_MODEL, related_name='post_like', blank=True)

    @property
    def publish(self):
        return self.publish_date

    def __str__(self):
        return self.title
