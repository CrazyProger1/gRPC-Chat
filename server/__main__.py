from concurrent import futures

import grpc

from gen import chat_pb2_grpc

from server.services.chat import ChatService

HOST, PORT = "localhost", 50052


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port(f"{HOST}:{PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
