import hashlib
import re
from datetime import datetime, timedelta

import jwt

from settings import settings


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def hash_password(password: str):
    # Use SHA-256 hash function
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed


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


def jwt_decode(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
