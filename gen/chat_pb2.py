# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gen/chat.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egen/chat.proto\"9\n\x14MessageCreateRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x13\n\x0breceiver_id\x18\x02 \x01(\x03\"(\n\x12MessageCreateReply\x12\x12\n\nmessage_id\x18\x01 \x01(\x03\"\x14\n\x12MessageReadRequest\"\x12\n\x10MessageReadReply2\x80\x01\n\x0b\x43hatService\x12;\n\rCreateMessage\x12\x15.MessageCreateRequest\x1a\x13.MessageCreateReply\x12\x34\n\nGetMessage\x12\x13.MessageReadRequest\x1a\x11.MessageReadReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gen.chat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGECREATEREQUEST']._serialized_start=18
  _globals['_MESSAGECREATEREQUEST']._serialized_end=75
  _globals['_MESSAGECREATEREPLY']._serialized_start=77
  _globals['_MESSAGECREATEREPLY']._serialized_end=117
  _globals['_MESSAGEREADREQUEST']._serialized_start=119
  _globals['_MESSAGEREADREQUEST']._serialized_end=139
  _globals['_MESSAGEREADREPLY']._serialized_start=141
  _globals['_MESSAGEREADREPLY']._serialized_end=159
  _globals['_CHATSERVICE']._serialized_start=162
  _globals['_CHATSERVICE']._serialized_end=290
# @@protoc_insertion_point(module_scope)
