from account.models import User


def authenticated_jwt(email, password):
    try:
        user = User.object.get()

    except User.DoesNotExist:
        pass
