import hashlib


def hash_password(password: str, secret_key: str):
    return hashlib.sha512(
        password.encode("utf-8") + secret_key.encode("utf-8")
    ).hexdigest()
