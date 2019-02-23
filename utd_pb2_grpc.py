# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import utd_pb2 as utd__pb2


class recycleStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.TestEcho = channel.unary_unary(
        '/hackutd.recycle/TestEcho',
        request_serializer=utd__pb2.Status.SerializeToString,
        response_deserializer=utd__pb2.Reply.FromString,
        )


class recycleServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def TestEcho(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_recycleServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'TestEcho': grpc.unary_unary_rpc_method_handler(
          servicer.TestEcho,
          request_deserializer=utd__pb2.Status.FromString,
          response_serializer=utd__pb2.Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hackutd.recycle', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
