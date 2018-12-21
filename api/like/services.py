from django.contrib.contenttypes.models import ContentType

from .models import Like
from api.account.models import User


def add_like(obj, user):
    """
    Like "obj"

    :param obj:
    :param user:
    :return: like
    """
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type, user=user, objects_id=obj.id)

    return like


def remove_like(obj, user):
    """
    Remove Like
    :param obj:
    :param user:
    """
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(
        content_type=obj_type, user=user, objects_id=obj.id
    ).delete()


def is_fan(obj, user) -> bool:
    """
    Check, liked 'user' 'obj'
    :param obj:
    :param user:
    :return: bool
    """
    if not user.is_authenticated:
        return False

    obj_type = ContentType.objects.get_for_model(obj)
    likes = Like(
        content_type=obj_type, user=user, objects_id=obj.id
    )
    return likes.exists()


def get_fans(obj):
    """
    Get all user who liked
    :param obj:
    :return: User Query
    """
    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        likes__content_type=obj_type, likes__object_id=obj.id
    )
