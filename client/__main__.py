import grpc
from grpc_health.v1 import health_pb2, health_pb2_grpc


def health_check_call(stub: health_pb2_grpc.HealthStub, service: str):
    request = health_pb2.HealthCheckRequest(service=service)
    resp = stub.Check(request)
    if resp.status == health_pb2.HealthCheckResponse.SERVING:
        print("server is serving")
    elif resp.status == health_pb2.HealthCheckResponse.NOT_SERVING:
        print("server stopped serving")


def main():
    with grpc.insecure_channel("localhost:50052") as channel:
        health_check_call(health_pb2_grpc.HealthStub(channel), service="ChatServicer")
        health_check_call(health_pb2_grpc.HealthStub(channel), service="AuthServicer")


if __name__ == "__main__":
    main()
