import logging
from typing import Callable

from gen import chat_pb2, chat_pb2_grpc
from server.database.repositories.message import MessageRepository
from server.services.healthy import HealthyServicer
from server.services.permissions import is_authenticated
from server.utils.logging import catch
from server.utils.permissions import permissions

logger = logging.getLogger("chat")


class ChatServicer(chat_pb2_grpc.ChatServicer, HealthyServicer):
    def __init__(self, repository: MessageRepository, set_health: Callable):
        self._repository = repository

        super().__init__(set_health=set_health)

    @catch(onlylog=True)
    @permissions(is_authenticated)
    def CreateMessage(self, request: chat_pb2.MessageCreateRequest, context, **kwargs):
        data = {
            "text": request.text,
            "receiver_id": request.receiver_id,
            "sender_id": context.user.id,
        }
        result = self._repository.create(data=data)
        return chat_pb2.MessageCreateReply(message_id=result.id)

    @catch(onlylog=True)
    @permissions(is_authenticated)
    def GetMessage(self, request: chat_pb2.MessageReadRequest, context, **kwargs):
        return chat_pb2.MessageReadReply()

    @catch(onlylog=True)
    @permissions(is_authenticated)
    def GetMessages(self, request: chat_pb2.MessagesFilteredRequest, context, **kwargs):
        yield

    @catch(onlylog=True)
    @permissions(is_authenticated)
    def UpdateMessage(self, request: chat_pb2.MessageUpdateRequest, context, **kwargs):
        return

    @catch(onlylog=True)
    @permissions(is_authenticated)
    def DeleteMessage(self, request: chat_pb2.MessageDeleteRequest, context, **kwargs):
        return
