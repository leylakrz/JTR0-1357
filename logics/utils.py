import hashlib
import re


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def hash_password(password: str):
    # Use SHA-256 hash function
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed
