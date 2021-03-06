# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from lcm_to_ros/can_coche_direccion.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class can_coche_direccion(genpy.Message):
  _md5sum = "2a77a418fbb4092f983b505954b450fd"
  _type = "lcm_to_ros/can_coche_direccion"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#######################################################################
# This message was automatically generated by the lcm_to_ros package
# https://github.com/nrjl/lcm_to_ros, nicholas.lawrance@oregonstate.edu
#######################################################################
#
# Source message:    .msg
# Creation:          lun 18 feb 2019 17:14:15 CET
#
#######################################################################
int32               timestamp_sec
int32               timestamp_nsec
float64             angulo_volante
float64             velocidad_volante
float64             angulo_columna
float64             velocidad_columna
float64             par_direccion
byte                flag_mensajes
"""
  __slots__ = ['timestamp_sec','timestamp_nsec','angulo_volante','velocidad_volante','angulo_columna','velocidad_columna','par_direccion','flag_mensajes']
  _slot_types = ['int32','int32','float64','float64','float64','float64','float64','byte']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp_sec,timestamp_nsec,angulo_volante,velocidad_volante,angulo_columna,velocidad_columna,par_direccion,flag_mensajes

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(can_coche_direccion, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timestamp_sec is None:
        self.timestamp_sec = 0
      if self.timestamp_nsec is None:
        self.timestamp_nsec = 0
      if self.angulo_volante is None:
        self.angulo_volante = 0.
      if self.velocidad_volante is None:
        self.velocidad_volante = 0.
      if self.angulo_columna is None:
        self.angulo_columna = 0.
      if self.velocidad_columna is None:
        self.velocidad_columna = 0.
      if self.par_direccion is None:
        self.par_direccion = 0.
      if self.flag_mensajes is None:
        self.flag_mensajes = 0
    else:
      self.timestamp_sec = 0
      self.timestamp_nsec = 0
      self.angulo_volante = 0.
      self.velocidad_volante = 0.
      self.angulo_columna = 0.
      self.velocidad_columna = 0.
      self.par_direccion = 0.
      self.flag_mensajes = 0

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
      buff.write(_get_struct_2i5db().pack(_x.timestamp_sec, _x.timestamp_nsec, _x.angulo_volante, _x.velocidad_volante, _x.angulo_columna, _x.velocidad_columna, _x.par_direccion, _x.flag_mensajes))
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
      end += 49
      (_x.timestamp_sec, _x.timestamp_nsec, _x.angulo_volante, _x.velocidad_volante, _x.angulo_columna, _x.velocidad_columna, _x.par_direccion, _x.flag_mensajes,) = _get_struct_2i5db().unpack(str[start:end])
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
      buff.write(_get_struct_2i5db().pack(_x.timestamp_sec, _x.timestamp_nsec, _x.angulo_volante, _x.velocidad_volante, _x.angulo_columna, _x.velocidad_columna, _x.par_direccion, _x.flag_mensajes))
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
      end += 49
      (_x.timestamp_sec, _x.timestamp_nsec, _x.angulo_volante, _x.velocidad_volante, _x.angulo_columna, _x.velocidad_columna, _x.par_direccion, _x.flag_mensajes,) = _get_struct_2i5db().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i5db = None
def _get_struct_2i5db():
    global _struct_2i5db
    if _struct_2i5db is None:
        _struct_2i5db = struct.Struct("<2i5db")
    return _struct_2i5db
