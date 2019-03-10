# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from lcm_to_ros/mobileye_alarmas.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class mobileye_alarmas(genpy.Message):
  _md5sum = "275230c90d76753bca3bff6115559522"
  _type = "lcm_to_ros/mobileye_alarmas"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#######################################################################
# This message was automatically generated by the lcm_to_ros package
# https://github.com/nrjl/lcm_to_ros, nicholas.lawrance@oregonstate.edu
#######################################################################
#
# Source message:    .msg
# Creation:          lun 18 feb 2019 17:14:16 CET
#
#######################################################################
int32               timestamp_sec
int32               timestamp_nsec
int16               flags
float32             headway
byte                warningLevel
"""
  __slots__ = ['timestamp_sec','timestamp_nsec','flags','headway','warningLevel']
  _slot_types = ['int32','int32','int16','float32','byte']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp_sec,timestamp_nsec,flags,headway,warningLevel

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(mobileye_alarmas, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timestamp_sec is None:
        self.timestamp_sec = 0
      if self.timestamp_nsec is None:
        self.timestamp_nsec = 0
      if self.flags is None:
        self.flags = 0
      if self.headway is None:
        self.headway = 0.
      if self.warningLevel is None:
        self.warningLevel = 0
    else:
      self.timestamp_sec = 0
      self.timestamp_nsec = 0
      self.flags = 0
      self.headway = 0.
      self.warningLevel = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2ihfb().pack(_x.timestamp_sec, _x.timestamp_nsec, _x.flags, _x.headway, _x.warningLevel))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 15
      (_x.timestamp_sec, _x.timestamp_nsec, _x.flags, _x.headway, _x.warningLevel,) = _get_struct_2ihfb().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2ihfb().pack(_x.timestamp_sec, _x.timestamp_nsec, _x.flags, _x.headway, _x.warningLevel))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 15
      (_x.timestamp_sec, _x.timestamp_nsec, _x.flags, _x.headway, _x.warningLevel,) = _get_struct_2ihfb().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2ihfb = None
def _get_struct_2ihfb():
    global _struct_2ihfb
    if _struct_2ihfb is None:
        _struct_2ihfb = struct.Struct("<2ihfb")
    return _struct_2ihfb
