import logging

from gen import chat_pb2, chat_pb2_grpc
from server.database.engine import engine
from server.database.repositories.message import MessageRepository

logger = logging.getLogger("chat")


class ChatService(chat_pb2_grpc.ChatService):
    def __init__(self):
        self._repository = MessageRepository(engine=engine)  # needed DI!!!

    def CreateMessage(self, request: chat_pb2.MessageCreateRequest, context, **kwargs):
        print(f"Message: {request.text}")
        data = {"text": request.text, "receiver_id": request.receiver_id}
        result = self._repository.create(data=data)
        return chat_pb2.MessageCreateReply(message_id=1)

    def GetMessage(self, request: chat_pb2.MessageReadRequest, context, **kwargs):
        return chat_pb2.MessageReadReply()

    def GetMessages(self, request: chat_pb2.MessagesFilteredRequest, context, **kwargs):
        yield

    def UpdateMessage(self, request: chat_pb2.MessageUpdateRequest, context, **kwargs):
        return

    def DeleteMessage(self, request: chat_pb2.MessageDeleteRequest, context, **kwargs):
        return
