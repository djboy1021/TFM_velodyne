# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from lcm_to_ros/estado_coche_LL.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class estado_coche_LL(genpy.Message):
  _md5sum = "e7c25e06970f89ceb6cf213885e085a4"
  _type = "lcm_to_ros/estado_coche_LL"
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
float64             tiempo
int8                calidad_gps
int8                nro_satelites
float64             UTM_x
float64             UTM_y
float64             orientacion
float64             velocidad
float64             aceleracion
float64             k_UTM_x
float64             k_UTM_y
float64             k_longitud
float64             k_latitud
float64             k_orientacion
float64             k_velocidad
float64             k_aceleracion
float64             angulo_volante
bool                flag_msg_gps
bool                flag_msg_canvel
bool                flag_msg_canvol
"""
  __slots__ = ['tiempo','calidad_gps','nro_satelites','UTM_x','UTM_y','orientacion','velocidad','aceleracion','k_UTM_x','k_UTM_y','k_longitud','k_latitud','k_orientacion','k_velocidad','k_aceleracion','angulo_volante','flag_msg_gps','flag_msg_canvel','flag_msg_canvol']
  _slot_types = ['float64','int8','int8','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       tiempo,calidad_gps,nro_satelites,UTM_x,UTM_y,orientacion,velocidad,aceleracion,k_UTM_x,k_UTM_y,k_longitud,k_latitud,k_orientacion,k_velocidad,k_aceleracion,angulo_volante,flag_msg_gps,flag_msg_canvel,flag_msg_canvol

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(estado_coche_LL, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.tiempo is None:
        self.tiempo = 0.
      if self.calidad_gps is None:
        self.calidad_gps = 0
      if self.nro_satelites is None:
        self.nro_satelites = 0
      if self.UTM_x is None:
        self.UTM_x = 0.
      if self.UTM_y is None:
        self.UTM_y = 0.
      if self.orientacion is None:
        self.orientacion = 0.
      if self.velocidad is None:
        self.velocidad = 0.
      if self.aceleracion is None:
        self.aceleracion = 0.
      if self.k_UTM_x is None:
        self.k_UTM_x = 0.
      if self.k_UTM_y is None:
        self.k_UTM_y = 0.
      if self.k_longitud is None:
        self.k_longitud = 0.
      if self.k_latitud is None:
        self.k_latitud = 0.
      if self.k_orientacion is None:
        self.k_orientacion = 0.
      if self.k_velocidad is None:
        self.k_velocidad = 0.
      if self.k_aceleracion is None:
        self.k_aceleracion = 0.
      if self.angulo_volante is None:
        self.angulo_volante = 0.
      if self.flag_msg_gps is None:
        self.flag_msg_gps = False
      if self.flag_msg_canvel is None:
        self.flag_msg_canvel = False
      if self.flag_msg_canvol is None:
        self.flag_msg_canvol = False
    else:
      self.tiempo = 0.
      self.calidad_gps = 0
      self.nro_satelites = 0
      self.UTM_x = 0.
      self.UTM_y = 0.
      self.orientacion = 0.
      self.velocidad = 0.
      self.aceleracion = 0.
      self.k_UTM_x = 0.
      self.k_UTM_y = 0.
      self.k_longitud = 0.
      self.k_latitud = 0.
      self.k_orientacion = 0.
      self.k_velocidad = 0.
      self.k_aceleracion = 0.
      self.angulo_volante = 0.
      self.flag_msg_gps = False
      self.flag_msg_canvel = False
      self.flag_msg_canvol = False

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
      buff.write(_get_struct_d2b13d3B().pack(_x.tiempo, _x.calidad_gps, _x.nro_satelites, _x.UTM_x, _x.UTM_y, _x.orientacion, _x.velocidad, _x.aceleracion, _x.k_UTM_x, _x.k_UTM_y, _x.k_longitud, _x.k_latitud, _x.k_orientacion, _x.k_velocidad, _x.k_aceleracion, _x.angulo_volante, _x.flag_msg_gps, _x.flag_msg_canvel, _x.flag_msg_canvol))
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
      end += 117
      (_x.tiempo, _x.calidad_gps, _x.nro_satelites, _x.UTM_x, _x.UTM_y, _x.orientacion, _x.velocidad, _x.aceleracion, _x.k_UTM_x, _x.k_UTM_y, _x.k_longitud, _x.k_latitud, _x.k_orientacion, _x.k_velocidad, _x.k_aceleracion, _x.angulo_volante, _x.flag_msg_gps, _x.flag_msg_canvel, _x.flag_msg_canvol,) = _get_struct_d2b13d3B().unpack(str[start:end])
      self.flag_msg_gps = bool(self.flag_msg_gps)
      self.flag_msg_canvel = bool(self.flag_msg_canvel)
      self.flag_msg_canvol = bool(self.flag_msg_canvol)
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
      buff.write(_get_struct_d2b13d3B().pack(_x.tiempo, _x.calidad_gps, _x.nro_satelites, _x.UTM_x, _x.UTM_y, _x.orientacion, _x.velocidad, _x.aceleracion, _x.k_UTM_x, _x.k_UTM_y, _x.k_longitud, _x.k_latitud, _x.k_orientacion, _x.k_velocidad, _x.k_aceleracion, _x.angulo_volante, _x.flag_msg_gps, _x.flag_msg_canvel, _x.flag_msg_canvol))
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
      end += 117
      (_x.tiempo, _x.calidad_gps, _x.nro_satelites, _x.UTM_x, _x.UTM_y, _x.orientacion, _x.velocidad, _x.aceleracion, _x.k_UTM_x, _x.k_UTM_y, _x.k_longitud, _x.k_latitud, _x.k_orientacion, _x.k_velocidad, _x.k_aceleracion, _x.angulo_volante, _x.flag_msg_gps, _x.flag_msg_canvel, _x.flag_msg_canvol,) = _get_struct_d2b13d3B().unpack(str[start:end])
      self.flag_msg_gps = bool(self.flag_msg_gps)
      self.flag_msg_canvel = bool(self.flag_msg_canvel)
      self.flag_msg_canvol = bool(self.flag_msg_canvol)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_d2b13d3B = None
def _get_struct_d2b13d3B():
    global _struct_d2b13d3B
    if _struct_d2b13d3B is None:
        _struct_d2b13d3B = struct.Struct("<d2b13d3B")
    return _struct_d2b13d3B
