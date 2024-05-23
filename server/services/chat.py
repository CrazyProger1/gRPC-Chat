from gen import chat_pb2, chat_pb2_grpc


class ChatService(chat_pb2_grpc.ChatService):
    def CreateMessage(self, request: chat_pb2.MessageCreateRequest, context, **kwargs):
        print(f"Message: {request.text}")
        return chat_pb2.MessageCreateReply(message_id=1)

    def GetMessage(self, request: chat_pb2.MessageReadRequest, context, **kwargs):
        return chat_pb2.MessageReadReply()
