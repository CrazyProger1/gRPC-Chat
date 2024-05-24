import datetime
import logging

import jwt

from .exceptions import JWTError

logger = logging.getLogger("chat")


def generate_token(
    payload: dict,
    secret_key: str,
    lifetime: datetime.timedelta = datetime.timedelta(days=1),
    algorithm: str = "HS256",
):
    data = {
        "exp": datetime.datetime.now(datetime.UTC) + lifetime,
        "iat": datetime.datetime.now(datetime.UTC),
    }
    data.update(payload)
    return jwt.encode(data, secret_key, algorithm=algorithm)


def decode_token(token: str, secret_key: str, algorithms=("HS256",)) -> dict:
    try:
        payload = jwt.decode(token, secret_key, algorithms=algorithms)
        return payload
    except jwt.ExpiredSignatureError:
        logger.info(f"Signature expired: {token}")
        raise JWTError("Signature expired")
    except jwt.InvalidTokenError:
        logger.info(f"Invalid token: {token}")
        raise JWTError("Invalid token")
