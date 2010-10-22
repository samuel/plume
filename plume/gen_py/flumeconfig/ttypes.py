#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *
import plume.gen_py.flumereportserver.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class FlumeNodeState(object):
  HELLO = 0
  IDLE = 1
  CONFIGURING = 2
  ACTIVE = 3
  ERROR = 4
  LOST = 5
  DECOMMISSIONED = 6

  _VALUES_TO_NAMES = {
    0: "HELLO",
    1: "IDLE",
    2: "CONFIGURING",
    3: "ACTIVE",
    4: "ERROR",
    5: "LOST",
    6: "DECOMMISSIONED",
  }

  _NAMES_TO_VALUES = {
    "HELLO": 0,
    "IDLE": 1,
    "CONFIGURING": 2,
    "ACTIVE": 3,
    "ERROR": 4,
    "LOST": 5,
    "DECOMMISSIONED": 6,
  }


class ThriftFlumeConfigData(object):
  """
  Attributes:
   - timestamp
   - sourceConfig
   - sinkConfig
   - sourceVersion
   - sinkVersion
   - flowID
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'timestamp', None, None, ), # 1
    (2, TType.STRING, 'sourceConfig', None, None, ), # 2
    (3, TType.STRING, 'sinkConfig', None, None, ), # 3
    (4, TType.I64, 'sourceVersion', None, None, ), # 4
    (5, TType.I64, 'sinkVersion', None, None, ), # 5
    (6, TType.STRING, 'flowID', None, None, ), # 6
  )

  def __init__(self, timestamp=None, sourceConfig=None, sinkConfig=None, sourceVersion=None, sinkVersion=None, flowID=None,):
    self.timestamp = timestamp
    self.sourceConfig = sourceConfig
    self.sinkConfig = sinkConfig
    self.sourceVersion = sourceVersion
    self.sinkVersion = sinkVersion
    self.flowID = flowID

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.timestamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.sourceConfig = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.sinkConfig = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.sourceVersion = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.sinkVersion = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.flowID = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ThriftFlumeConfigData')
    if self.timestamp != None:
      oprot.writeFieldBegin('timestamp', TType.I64, 1)
      oprot.writeI64(self.timestamp)
      oprot.writeFieldEnd()
    if self.sourceConfig != None:
      oprot.writeFieldBegin('sourceConfig', TType.STRING, 2)
      oprot.writeString(self.sourceConfig)
      oprot.writeFieldEnd()
    if self.sinkConfig != None:
      oprot.writeFieldBegin('sinkConfig', TType.STRING, 3)
      oprot.writeString(self.sinkConfig)
      oprot.writeFieldEnd()
    if self.sourceVersion != None:
      oprot.writeFieldBegin('sourceVersion', TType.I64, 4)
      oprot.writeI64(self.sourceVersion)
      oprot.writeFieldEnd()
    if self.sinkVersion != None:
      oprot.writeFieldBegin('sinkVersion', TType.I64, 5)
      oprot.writeI64(self.sinkVersion)
      oprot.writeFieldEnd()
    if self.flowID != None:
      oprot.writeFieldBegin('flowID', TType.STRING, 6)
      oprot.writeString(self.flowID)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
