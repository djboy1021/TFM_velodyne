# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from lcm_to_ros/occupancy_grid.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class occupancy_grid(genpy.Message):
  _md5sum = "41f67f04cae87b0293624c6fabb5025f"
  _type = "lcm_to_ros/occupancy_grid"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#######################################################################
# This message was automatically generated by the lcm_to_ros package
# https://github.com/nrjl/lcm_to_ros, nicholas.lawrance@oregonstate.edu
#######################################################################
#
# Source message:    .msg
# Creation:          lun 18 feb 2019 17:14:17 CET
#
#######################################################################
int32               width
int32               height
float32             d_lat
float32             d_long
int32               n_data
float32             resolution
int8[]              data
"""
  __slots__ = ['width','height','d_lat','d_long','n_data','resolution','data']
  _slot_types = ['int32','int32','float32','float32','int32','float32','int8[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       width,height,d_lat,d_long,n_data,resolution,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(occupancy_grid, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.width is None:
        self.width = 0
      if self.height is None:
        self.height = 0
      if self.d_lat is None:
        self.d_lat = 0.
      if self.d_long is None:
        self.d_long = 0.
      if self.n_data is None:
        self.n_data = 0
      if self.resolution is None:
        self.resolution = 0.
      if self.data is None:
        self.data = []
    else:
      self.width = 0
      self.height = 0
      self.d_lat = 0.
      self.d_long = 0.
      self.n_data = 0
      self.resolution = 0.
      self.data = []

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
      buff.write(_get_struct_2i2fif().pack(_x.width, _x.height, _x.d_lat, _x.d_long, _x.n_data, _x.resolution))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(struct.pack(pattern, *self.data))
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
      end += 24
      (_x.width, _x.height, _x.d_lat, _x.d_long, _x.n_data, _x.resolution,) = _get_struct_2i2fif().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.data = struct.unpack(pattern, str[start:end])
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
      buff.write(_get_struct_2i2fif().pack(_x.width, _x.height, _x.d_lat, _x.d_long, _x.n_data, _x.resolution))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(self.data.tostring())
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
      end += 24
      (_x.width, _x.height, _x.d_lat, _x.d_long, _x.n_data, _x.resolution,) = _get_struct_2i2fif().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.data = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i2fif = None
def _get_struct_2i2fif():
    global _struct_2i2fif
    if _struct_2i2fif is None:
        _struct_2i2fif = struct.Struct("<2i2fif")
    return _struct_2i2fif