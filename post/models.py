from django.db import models

from account.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    title = models.CharField(max_length=99)
    body = models.TextField(max_length=500)
    publish_date = models.DateTimeField(auto_now_add=True)

    @property
    def publish(self):
        return self.publish_date

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post')
    created = models.DateTimeField(auto_now_add=True)
