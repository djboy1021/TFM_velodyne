# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from lcm_to_ros/osm_route_result.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import lcm_to_ros.msg

class osm_route_result(genpy.Message):
  _md5sum = "1e17e3fc432d0f2c2a93661fa8d61a75"
  _type = "lcm_to_ros/osm_route_result"
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
int32               id
int32               n_puntos
osm_waypoint[]      puntos

================================================================================
MSG: lcm_to_ros/osm_waypoint
#######################################################################
# This message was automatically generated by the lcm_to_ros package
# https://github.com/nrjl/lcm_to_ros, nicholas.lawrance@oregonstate.edu
#######################################################################
#
# Source message:    .msg
# Creation:          lun 18 feb 2019 17:14:17 CET
#
#######################################################################
float64             latitud
float64             longitud
float64             orientacion
"""
  __slots__ = ['id','n_puntos','puntos']
  _slot_types = ['int32','int32','lcm_to_ros/osm_waypoint[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,n_puntos,puntos

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(osm_route_result, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.n_puntos is None:
        self.n_puntos = 0
      if self.puntos is None:
        self.puntos = []
    else:
      self.id = 0
      self.n_puntos = 0
      self.puntos = []

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
      buff.write(_get_struct_2i().pack(_x.id, _x.n_puntos))
      length = len(self.puntos)
      buff.write(_struct_I.pack(length))
      for val1 in self.puntos:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.latitud, _x.longitud, _x.orientacion))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.puntos is None:
        self.puntos = None
      end = 0
      _x = self
      start = end
      end += 8
      (_x.id, _x.n_puntos,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.puntos = []
      for i in range(0, length):
        val1 = lcm_to_ros.msg.osm_waypoint()
        _x = val1
        start = end
        end += 24
        (_x.latitud, _x.longitud, _x.orientacion,) = _get_struct_3d().unpack(str[start:end])
        self.puntos.append(val1)
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
      buff.write(_get_struct_2i().pack(_x.id, _x.n_puntos))
      length = len(self.puntos)
      buff.write(_struct_I.pack(length))
      for val1 in self.puntos:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.latitud, _x.longitud, _x.orientacion))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.puntos is None:
        self.puntos = None
      end = 0
      _x = self
      start = end
      end += 8
      (_x.id, _x.n_puntos,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.puntos = []
      for i in range(0, length):
        val1 = lcm_to_ros.msg.osm_waypoint()
        _x = val1
        start = end
        end += 24
        (_x.latitud, _x.longitud, _x.orientacion,) = _get_struct_3d().unpack(str[start:end])
        self.puntos.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
