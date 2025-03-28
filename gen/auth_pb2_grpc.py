# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from gen import auth_pb2 as gen_dot_auth__pb2

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
        + f' but the generated code in gen/auth_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class AuthServicerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterUser = channel.unary_unary(
                '/AuthServicer/RegisterUser',
                request_serializer=gen_dot_auth__pb2.UserRegisterRequest.SerializeToString,
                response_deserializer=gen_dot_auth__pb2.UserRegisterReply.FromString,
                _registered_method=True)
        self.LoginUser = channel.unary_unary(
                '/AuthServicer/LoginUser',
                request_serializer=gen_dot_auth__pb2.UserLoginRequest.SerializeToString,
                response_deserializer=gen_dot_auth__pb2.UserLoginReply.FromString,
                _registered_method=True)
        self.RefreshUserToken = channel.unary_unary(
                '/AuthServicer/RefreshUserToken',
                request_serializer=gen_dot_auth__pb2.RefreshUserTokenRequest.SerializeToString,
                response_deserializer=gen_dot_auth__pb2.RefreshUserTokenReply.FromString,
                _registered_method=True)


class AuthServicerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoginUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RefreshUserToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServicerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterUser,
                    request_deserializer=gen_dot_auth__pb2.UserRegisterRequest.FromString,
                    response_serializer=gen_dot_auth__pb2.UserRegisterReply.SerializeToString,
            ),
            'LoginUser': grpc.unary_unary_rpc_method_handler(
                    servicer.LoginUser,
                    request_deserializer=gen_dot_auth__pb2.UserLoginRequest.FromString,
                    response_serializer=gen_dot_auth__pb2.UserLoginReply.SerializeToString,
            ),
            'RefreshUserToken': grpc.unary_unary_rpc_method_handler(
                    servicer.RefreshUserToken,
                    request_deserializer=gen_dot_auth__pb2.RefreshUserTokenRequest.FromString,
                    response_serializer=gen_dot_auth__pb2.RefreshUserTokenReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AuthServicer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('AuthServicer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AuthServicer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterUser(request,
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
            '/AuthServicer/RegisterUser',
            gen_dot_auth__pb2.UserRegisterRequest.SerializeToString,
            gen_dot_auth__pb2.UserRegisterReply.FromString,
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
    def LoginUser(request,
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
            '/AuthServicer/LoginUser',
            gen_dot_auth__pb2.UserLoginRequest.SerializeToString,
            gen_dot_auth__pb2.UserLoginReply.FromString,
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
    def RefreshUserToken(request,
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
            '/AuthServicer/RefreshUserToken',
            gen_dot_auth__pb2.RefreshUserTokenRequest.SerializeToString,
            gen_dot_auth__pb2.RefreshUserTokenReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
