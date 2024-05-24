import logging
from typing import Callable

import grpc

from gen import chat_pb2, chat_pb2_grpc
from server.database.repositories.message import MessageRepository
from server.database.repositories.user import UserRepository
from server.servicers.healthy import HealthyServicer
from server.servicers.permissions import is_authenticated
from server.utils.logging import catch
from server.utils.permissions import permissions

logger = logging.getLogger("chat")


class ChatServicer(chat_pb2_grpc.ChatServicer, HealthyServicer):
    def __init__(
            self,
            message_repository: MessageRepository,
            user_repository: UserRepository,
            set_health: Callable,
    ):
        self._message_repository = message_repository
        self._user_repository = user_repository

        super().__init__(set_health=set_health)

    def check_message(self, pk: any):
        pass

    @catch(onlylog=True)
    @permissions(is_authenticated)
    def CreateMessage(self, request: chat_pb2.MessageCreateRequest, context, **kwargs):
        if not self._user_repository.exists(id=request.receiver_id):
            context.abort(grpc.StatusCode.NOT_FOUND, "User not found")

        data = {
            "text": request.text,
            "receiver_id": request.receiver_id,
            "sender_id": context.user.id,
        }
        result = self._message_repository.create(data=data)
        return chat_pb2.MessageCreateReply(message_id=result.id)

    @catch(onlylog=True)
    @permissions(is_authenticated)
    def GetMessage(self, request: chat_pb2.MessageReadRequest, context, **kwargs):
        message = self._message_repository.read(pk=request.message_id)

        if not message:
            context.abort(grpc.StatusCode.NOT_FOUND, "Message not found")

        if context.user.id not in {message.receiver_id, message.sender_id}:
            context.abort(grpc.StatusCode.PERMISSION_DENIED, "Not your message")

        return chat_pb2.MessageReadReply(
            message_id=message.id, text=message.text, sender_id=message.sender_id,
        )

    @catch(onlylog=True)
    @permissions(is_authenticated)
    def GetMessages(self, request: chat_pb2.MessagesFilteredRequest, context, **kwargs):
        for message in self._message_repository.read_many(receiver_id=context.user.id):
            yield chat_pb2.MessageReadReply(
                message_id=message.id, text=message.text, sender_id=message.sender_id,
            )

    @catch(onlylog=True)
    @permissions(is_authenticated)
    def UpdateMessage(self, request: chat_pb2.MessageUpdateRequest, context, **kwargs):
        if not self._message_repository.exists(id=request.message_id):
            context.abort(grpc.StatusCode.NOT_FOUND, "Message not found")

        self._message_repository.update(request.message_id, {"text": request.text})
        return chat_pb2.MessageUpdateReply()

    @catch(onlylog=True)
    @permissions(is_authenticated)
    def DeleteMessage(self, request: chat_pb2.MessageDeleteRequest, context, **kwargs):
        if not self._message_repository.exists(id=request.message_id):
            context.abort(grpc.StatusCode.NOT_FOUND, "Message not found")

        self._message_repository.delete(pk=request.message_id)

        return chat_pb2.MessageDeleteReply()
