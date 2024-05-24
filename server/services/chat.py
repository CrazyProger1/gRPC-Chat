import logging

from gen import chat_pb2, chat_pb2_grpc
from server.database.repositories.message import MessageRepository
from server.services.permissions import is_authenticated
from server.utils.permissions import permissions
from server.utils.logging import catch

logger = logging.getLogger("chat")


class ChatService(chat_pb2_grpc.ChatService):
    def __init__(self, repository: MessageRepository):
        self._repository = repository

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
    def GetMessage(self, request: chat_pb2.MessageReadRequest, context, **kwargs):
        return chat_pb2.MessageReadReply()

    @catch(onlylog=True)
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
