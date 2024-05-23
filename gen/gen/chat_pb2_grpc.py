# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from gen import chat_pb2 as gen_dot_chat__pb2

GRPC_GENERATED_VERSION = '1.64.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in gen/chat_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ChatServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateMessage = channel.unary_unary(
                '/ChatService/CreateMessage',
                request_serializer=gen_dot_chat__pb2.MessageCreateRequest.SerializeToString,
                response_deserializer=gen_dot_chat__pb2.MessageCreateReply.FromString,
                _registered_method=True)
        self.GetMessage = channel.unary_unary(
                '/ChatService/GetMessage',
                request_serializer=gen_dot_chat__pb2.MessageReadRequest.SerializeToString,
                response_deserializer=gen_dot_chat__pb2.MessageReadReply.FromString,
                _registered_method=True)


class ChatServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateMessage,
                    request_deserializer=gen_dot_chat__pb2.MessageCreateRequest.FromString,
                    response_serializer=gen_dot_chat__pb2.MessageCreateReply.SerializeToString,
            ),
            'GetMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMessage,
                    request_deserializer=gen_dot_chat__pb2.MessageReadRequest.FromString,
                    response_serializer=gen_dot_chat__pb2.MessageReadReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ChatService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ChatService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ChatService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ChatService/CreateMessage',
            gen_dot_chat__pb2.MessageCreateRequest.SerializeToString,
            gen_dot_chat__pb2.MessageCreateReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ChatService/GetMessage',
            gen_dot_chat__pb2.MessageReadRequest.SerializeToString,
            gen_dot_chat__pb2.MessageReadReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
