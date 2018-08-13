# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import src.authentification_pb2 as authentification__pb2


class AuthServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SignIn = channel.unary_unary(
        '/grpc.auth.AuthService/SignIn',
        request_serializer=authentification__pb2.Request.SerializeToString,
        response_deserializer=authentification__pb2.Response.FromString,
        )


class AuthServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SignIn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SignIn': grpc.unary_unary_rpc_method_handler(
          servicer.SignIn,
          request_deserializer=authentification__pb2.Request.FromString,
          response_serializer=authentification__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.auth.AuthService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
