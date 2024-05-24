import grpc


def is_authenticated(service, request, context, **kwargs):
    if context.user is None:
        context.abort(grpc.StatusCode.UNAUTHENTICATED, "Unauthenticated")
    return True
