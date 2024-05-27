import logging
from typing import Callable

import grpc

from gen import auth_pb2, auth_pb2_grpc
from server.config import JWT_ACCESS_LIFETIME, JWT_REFRESH_LIFETIME, SECRET
from server.database.repositories.user import UserRepository
from server.servicers.healthy import HealthyServicer
from server.utils.exceptions import JWTError
from server.utils.jwt import decode_token, generate_token
from server.utils.logging import catch
from server.utils.password import hash_password

logger = logging.getLogger("chat")


class AuthServicer(auth_pb2_grpc.AuthServicer, HealthyServicer):
    def __init__(self, user_repository: UserRepository, set_health: Callable):
        self._user_repository = user_repository

        super().__init__(set_health=set_health)

    @catch(onlylog=True)
    def RegisterUser(self, request: auth_pb2.UserRegisterRequest, context, **kwargs):
        hashed_password = hash_password(request.password, secret_key=SECRET)

        self._user_repository.create(
            {
                "email": request.email,
                "nickname": request.nickname,
                "hashed_password": hashed_password,
            }
        )
        logger.info(f"User registered: {request.email}")
        return auth_pb2.UserRegisterReply()

    @catch(onlylog=True)
    def LoginUser(self, request: auth_pb2.UserLoginRequest, context, **kwargs):
        user = self._user_repository.read_by(email=request.email)

        access = generate_token(
            payload={"id": user.id, "type": "access"},
            secret_key=SECRET,
            lifetime=JWT_ACCESS_LIFETIME,
        )
        refresh = generate_token(
            payload={"id": user.id, "type": "refresh"},
            secret_key=SECRET,
            lifetime=JWT_REFRESH_LIFETIME,
        )
        logger.info(f"User logged in: {request.email}")
        return auth_pb2.UserLoginReply(access=access, refresh=refresh)

    @catch(onlylog=True)
    def RefreshUserToken(self, request: auth_pb2.RefreshUserTokenRequest, context, **kwargs):
        refresh = request.refresh

        try:
            payload = decode_token(token=refresh, secret_key=SECRET)
            if payload.get("type") != "refresh":
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Invalid refresh")

            user = self._user_repository.read(pk=payload["id"])
            access = generate_token(
                payload={"id": user.id, "type": "access"},
                secret_key=SECRET,
                lifetime=JWT_ACCESS_LIFETIME,
            )
            return auth_pb2.RefreshUserTokenReply(access=access)
        except JWTError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))
