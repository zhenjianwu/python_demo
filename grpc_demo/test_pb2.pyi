from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MsgBatch(_message.Message):
    __slots__ = ["code", "data", "msg"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    code: int
    data: str
    msg: str
    def __init__(self, code: _Optional[int] = ..., msg: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class Req(_message.Message):
    __slots__ = ["cmd", "params"]
    CMD_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    cmd: str
    params: str
    def __init__(self, cmd: _Optional[str] = ..., params: _Optional[str] = ...) -> None: ...
