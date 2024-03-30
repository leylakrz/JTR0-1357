import hashlib


def hash_password(password: str):
    # Use SHA-256 hash function
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed
