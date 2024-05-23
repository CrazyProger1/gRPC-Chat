from typing import ClassVar as _ClassVar
from typing import Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class MessageCreateRequest(_message.Message):
    __slots__ = ("text", "receiver_id")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_ID_FIELD_NUMBER: _ClassVar[int]
    text: str
    receiver_id: int
    def __init__(
        self, text: _Optional[str] = ..., receiver_id: _Optional[int] = ...
    ) -> None: ...

class MessageCreateReply(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    def __init__(self, message_id: _Optional[int] = ...) -> None: ...

class MessageReadRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MessageReadReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
