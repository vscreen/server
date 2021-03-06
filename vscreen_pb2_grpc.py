# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import vscreen_pb2 as vscreen__pb2


class VScreenStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Auth = channel.unary_unary(
        '/VScreen/Auth',
        request_serializer=vscreen__pb2.Credential.SerializeToString,
        response_deserializer=vscreen__pb2.Status.FromString,
        )
    self.Play = channel.unary_unary(
        '/VScreen/Play',
        request_serializer=vscreen__pb2.Empty.SerializeToString,
        response_deserializer=vscreen__pb2.Status.FromString,
        )
    self.Pause = channel.unary_unary(
        '/VScreen/Pause',
        request_serializer=vscreen__pb2.Empty.SerializeToString,
        response_deserializer=vscreen__pb2.Status.FromString,
        )
    self.Stop = channel.unary_unary(
        '/VScreen/Stop',
        request_serializer=vscreen__pb2.Empty.SerializeToString,
        response_deserializer=vscreen__pb2.Status.FromString,
        )
    self.Next = channel.unary_unary(
        '/VScreen/Next',
        request_serializer=vscreen__pb2.Empty.SerializeToString,
        response_deserializer=vscreen__pb2.Status.FromString,
        )
    self.Add = channel.unary_unary(
        '/VScreen/Add',
        request_serializer=vscreen__pb2.Source.SerializeToString,
        response_deserializer=vscreen__pb2.Status.FromString,
        )
    self.Seek = channel.unary_unary(
        '/VScreen/Seek',
        request_serializer=vscreen__pb2.Position.SerializeToString,
        response_deserializer=vscreen__pb2.Status.FromString,
        )
    self.Subscribe = channel.unary_stream(
        '/VScreen/Subscribe',
        request_serializer=vscreen__pb2.User.SerializeToString,
        response_deserializer=vscreen__pb2.Info.FromString,
        )
    self.Unsubscribe = channel.unary_unary(
        '/VScreen/Unsubscribe',
        request_serializer=vscreen__pb2.User.SerializeToString,
        response_deserializer=vscreen__pb2.Status.FromString,
        )


class VScreenServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Auth(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Play(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Pause(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Next(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Add(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Seek(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Subscribe(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Unsubscribe(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_VScreenServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Auth': grpc.unary_unary_rpc_method_handler(
          servicer.Auth,
          request_deserializer=vscreen__pb2.Credential.FromString,
          response_serializer=vscreen__pb2.Status.SerializeToString,
      ),
      'Play': grpc.unary_unary_rpc_method_handler(
          servicer.Play,
          request_deserializer=vscreen__pb2.Empty.FromString,
          response_serializer=vscreen__pb2.Status.SerializeToString,
      ),
      'Pause': grpc.unary_unary_rpc_method_handler(
          servicer.Pause,
          request_deserializer=vscreen__pb2.Empty.FromString,
          response_serializer=vscreen__pb2.Status.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=vscreen__pb2.Empty.FromString,
          response_serializer=vscreen__pb2.Status.SerializeToString,
      ),
      'Next': grpc.unary_unary_rpc_method_handler(
          servicer.Next,
          request_deserializer=vscreen__pb2.Empty.FromString,
          response_serializer=vscreen__pb2.Status.SerializeToString,
      ),
      'Add': grpc.unary_unary_rpc_method_handler(
          servicer.Add,
          request_deserializer=vscreen__pb2.Source.FromString,
          response_serializer=vscreen__pb2.Status.SerializeToString,
      ),
      'Seek': grpc.unary_unary_rpc_method_handler(
          servicer.Seek,
          request_deserializer=vscreen__pb2.Position.FromString,
          response_serializer=vscreen__pb2.Status.SerializeToString,
      ),
      'Subscribe': grpc.unary_stream_rpc_method_handler(
          servicer.Subscribe,
          request_deserializer=vscreen__pb2.User.FromString,
          response_serializer=vscreen__pb2.Info.SerializeToString,
      ),
      'Unsubscribe': grpc.unary_unary_rpc_method_handler(
          servicer.Unsubscribe,
          request_deserializer=vscreen__pb2.User.FromString,
          response_serializer=vscreen__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'VScreen', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
