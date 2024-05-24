from gen import auth_pb2, auth_pb2_grpc
from server.config import SECRET, JWT_ACCESS_LIFETIME, JWT_REFRESH_LIFETIME
from server.database.engine import engine
from server.database.repositories.user import UserRepository
from server.utils.password import hash_password
from server.utils.jwt import generate_token, decode_token


class AuthService(auth_pb2_grpc.AuthService):
    def __init__(self):
        self._repository = UserRepository(engine=engine)  # needed DI!!!

    def RegisterUser(self, request: auth_pb2.UserRegisterRequest, context, **kwargs):
        hashed_password = hash_password(request.password, secret_key=SECRET)

        self._repository.create(
            {
                "email": request.email,
                "nickname": request.nickname,
                "hashed_password": hashed_password,
            }
        )
        return auth_pb2.UserRegisterReply()

    def LoginUser(self, request: auth_pb2.UserLoginRequest, context, **kwargs):
        user = self._repository.read_by("email", request.email)

        access = generate_token(
            payload={"id": user.id, "type": "access"},
            secret_key=SECRET,
            lifetime=JWT_ACCESS_LIFETIME
        )
        refresh = generate_token(
            payload={"id": user.id, "type": "refresh"},
            secret_key=SECRET,
            lifetime=JWT_REFRESH_LIFETIME
        )

        return auth_pb2.UserLoginReply(access=access, refresh=refresh)

    def RefreshUserToken(self, request: auth_pb2.UserLoginRequest, context, **kwargs):
        return auth_pb2.RefreshUserTokenReply()
