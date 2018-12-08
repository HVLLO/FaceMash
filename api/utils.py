from django.contrib.auth import user_logged_in

from rest_framework_jwt.serializers import jwt_payload_handler

import jwt

from root.settings import SECRET_KEY
from account.models import User


def authenticated_jwt(email, password, request):
    """
    This function create JWT for user if user exist,

    return: dictionary with info JWT
    return: dictionary with info

    :param email:
    :param password:
    :param request:
    :return: Boolean value
    """
    try:
        user = User.object.get(email=email, password=password)
        user_details = {}

        if user:
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, SECRET_KEY)
            user_details['name'] = "%s %s" % (
                user.first_name, user.last_name)
            user_details['token'] = token
            user_logged_in.send(sender=user.__class__,
                                request=request, user=user)

            return user_details

        # TODO: To Remake!
        else:
            # return {'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return None

    # TODO: To Remake!
    except User.DoesNotExist:
        # return {'error': 'please provide a email and a password'}
        return None
