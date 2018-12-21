from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from root.settings import AUTH_USER_MODEL


# This model refer to the generic type of model
class Like(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='user_like',
                             blank=True, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    objects_id = models.PositiveIntegerField()
    content_objects = GenericForeignKey('content_type', 'objects_id')

