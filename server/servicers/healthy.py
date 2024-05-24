from typing import Callable

from grpc_health.v1 import health_pb2


class HealthyServicer:
    def __init__(self, set_health: Callable):
        self.set_health = set_health
        set_health(type(self).__name__, health_pb2.HealthCheckResponse.SERVING)
