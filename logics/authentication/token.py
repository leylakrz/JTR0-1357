from datetime import datetime, timedelta

import jwt

from settings import settings


def generate_access_token(user_id):
    payload = {
        "uid": user_id,
        "exp": datetime.now() + timedelta(**settings.ACCESS_TOKEN_EXP)
    }
    return jwt_encode(payload)


def jwt_encode(payload):
    """
    document:
        https://pyjwt.readthedocs.io/en/latest/
    """
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
