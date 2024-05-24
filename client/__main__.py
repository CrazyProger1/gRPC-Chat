import grpc

from gen import chat_pb2, chat_pb2_grpc


def main():
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = chat_pb2_grpc.ChatServiceStub(channel)
        response = stub.CreateMessage(
            chat_pb2.MessageCreateRequest(text="Hello world!")
        )

        print(response)


if __name__ == "__main__":
    main()
