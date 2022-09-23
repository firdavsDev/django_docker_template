from rest_framework.authtoken.models import Token

from ...account.models import User
from ...common.utils import FAILURE_BODY, SUCCESS_BODY


def login(email: str, password: str):
    user = User.objects.filter(email=email)
    if user.exists() is False:
        additional_data = dict(message="login failed, incorrect login or password")
        SUCCESS_BODY.update(**additional_data)
        return FAILURE_BODY

    user = User.objects.filter(email=email).first()
    if user.check_password(password) is False:
        additional_data = dict(message="login failed, incorrect login or password")
        SUCCESS_BODY.update(**additional_data)
        return FAILURE_BODY

    token, _ = Token.objects.get_or_create(user=user)
    additional_data = dict(id=user.id, token=token.key)
    SUCCESS_BODY.update(**additional_data)
    return SUCCESS_BODY
