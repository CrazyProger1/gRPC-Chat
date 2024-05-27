from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserRegisterRequest(_message.Message):
    __slots__ = ("email", "nickname", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    nickname: str
    password: str
    def __init__(self, email: _Optional[str] = ..., nickname: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class UserRegisterReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UserLoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class UserLoginReply(_message.Message):
    __slots__ = ("access", "refresh")
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    access: str
    refresh: str
    def __init__(self, access: _Optional[str] = ..., refresh: _Optional[str] = ...) -> None: ...

class RefreshUserTokenRequest(_message.Message):
    __slots__ = ("refresh",)
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    refresh: str
    def __init__(self, refresh: _Optional[str] = ...) -> None: ...

class RefreshUserTokenReply(_message.Message):
    __slots__ = ("access",)
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    access: str
    def __init__(self, access: _Optional[str] = ...) -> None: ...
