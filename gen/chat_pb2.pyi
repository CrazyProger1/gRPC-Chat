from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MessageCreateRequest(_message.Message):
    __slots__ = ("text", "receiver_id")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_ID_FIELD_NUMBER: _ClassVar[int]
    text: str
    receiver_id: int
    def __init__(self, text: _Optional[str] = ..., receiver_id: _Optional[int] = ...) -> None: ...

class MessageCreateReply(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    def __init__(self, message_id: _Optional[int] = ...) -> None: ...

class MessageReadRequest(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    def __init__(self, message_id: _Optional[int] = ...) -> None: ...

class MessagesFilteredRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MessageReadReply(_message.Message):
    __slots__ = ("message_id", "text", "sender_id")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    text: str
    sender_id: int
    def __init__(self, message_id: _Optional[int] = ..., text: _Optional[str] = ..., sender_id: _Optional[int] = ...) -> None: ...

class MessageUpdateRequest(_message.Message):
    __slots__ = ("message_id", "text")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    text: str
    def __init__(self, message_id: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class MessageUpdateReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MessageDeleteRequest(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    def __init__(self, message_id: _Optional[int] = ...) -> None: ...

class MessageDeleteReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
