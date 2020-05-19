# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProtobufRpcEngine.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ProtobufRpcEngine.proto',
  package='hadoop.common',
  syntax='proto2',
  serialized_options=b'\n\036org.apache.hadoop.ipc.protobufB\027ProtobufRpcEngineProtos\240\001\001',
  serialized_pb=b'\n\x17ProtobufRpcEngine.proto\x12\rhadoop.common\"k\n\x12RequestHeaderProto\x12\x12\n\nmethodName\x18\x01 \x02(\t\x12\"\n\x1a\x64\x65\x63laringClassProtocolName\x18\x02 \x02(\t\x12\x1d\n\x15\x63lientProtocolVersion\x18\x03 \x02(\x04\x42<\n\x1eorg.apache.hadoop.ipc.protobufB\x17ProtobufRpcEngineProtos\xa0\x01\x01'
)




_REQUESTHEADERPROTO = _descriptor.Descriptor(
  name='RequestHeaderProto',
  full_name='hadoop.common.RequestHeaderProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='methodName', full_name='hadoop.common.RequestHeaderProto.methodName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='declaringClassProtocolName', full_name='hadoop.common.RequestHeaderProto.declaringClassProtocolName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientProtocolVersion', full_name='hadoop.common.RequestHeaderProto.clientProtocolVersion', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['RequestHeaderProto'] = _REQUESTHEADERPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestHeaderProto = _reflection.GeneratedProtocolMessageType('RequestHeaderProto', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTHEADERPROTO,
  '__module__' : 'ProtobufRpcEngine_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.common.RequestHeaderProto)
  })
_sym_db.RegisterMessage(RequestHeaderProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
