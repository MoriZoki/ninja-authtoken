from collections import namedtuple
from django.contrib.auth.hashers import check_password, make_password


from ninja.security import APIKeyHeader
from .models import APIKey





def check_apikey(api_key: str):
    if not api_key:
        return False

    token = APIKey.objects.filter(token=api_key).first()
    
    if not token:
        return False

    user = token.user

    if not user:
        return False

    if not user.is_active:
        return False

    return user


class APIKeyAuth(APIKeyHeader):
    param_name = "Authorization"

    def authenticate(self, request, key):
        user = check_apikey(key)

        if not user:
            return False

        request.user = user
        return user
