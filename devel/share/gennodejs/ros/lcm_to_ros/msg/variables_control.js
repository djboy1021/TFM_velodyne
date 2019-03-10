// Auto-generated. Do not edit!

// (in-package lcm_to_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class variables_control {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.tiempo = null;
      this.deriva = null;
      this.cabeceo = null;
      this.curvatura = null;
      this.velocidad = null;
      this.velocidad_consigna = null;
    }
    else {
      if (initObj.hasOwnProperty('tiempo')) {
        this.tiempo = initObj.tiempo
      }
      else {
        this.tiempo = 0.0;
      }
      if (initObj.hasOwnProperty('deriva')) {
        this.deriva = initObj.deriva
      }
      else {
        this.deriva = 0.0;
      }
      if (initObj.hasOwnProperty('cabeceo')) {
        this.cabeceo = initObj.cabeceo
      }
      else {
        this.cabeceo = 0.0;
      }
      if (initObj.hasOwnProperty('curvatura')) {
        this.curvatura = initObj.curvatura
      }
      else {
        this.curvatura = 0.0;
      }
      if (initObj.hasOwnProperty('velocidad')) {
        this.velocidad = initObj.velocidad
      }
      else {
        this.velocidad = 0.0;
      }
      if (initObj.hasOwnProperty('velocidad_consigna')) {
        this.velocidad_consigna = initObj.velocidad_consigna
      }
      else {
        this.velocidad_consigna = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type variables_control
    // Serialize message field [tiempo]
    bufferOffset = _serializer.float64(obj.tiempo, buffer, bufferOffset);
    // Serialize message field [deriva]
    bufferOffset = _serializer.float64(obj.deriva, buffer, bufferOffset);
    // Serialize message field [cabeceo]
    bufferOffset = _serializer.float64(obj.cabeceo, buffer, bufferOffset);
    // Serialize message field [curvatura]
    bufferOffset = _serializer.float64(obj.curvatura, buffer, bufferOffset);
    // Serialize message field [velocidad]
    bufferOffset = _serializer.float64(obj.velocidad, buffer, bufferOffset);
    // Serialize message field [velocidad_consigna]
    bufferOffset = _serializer.float64(obj.velocidad_consigna, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type variables_control
    let len;
    let data = new variables_control(null);
    // Deserialize message field [tiempo]
    data.tiempo = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [deriva]
    data.deriva = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [cabeceo]
    data.cabeceo = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [curvatura]
    data.curvatura = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [velocidad]
    data.velocidad = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [velocidad_consigna]
    data.velocidad_consigna = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 48;
  }

  static datatype() {
    // Returns string type for a message object
    return 'lcm_to_ros/variables_control';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3d53f02eaa996b1eb6728f13ae0c3580';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #######################################################################
    # This message was automatically generated by the lcm_to_ros package
    # https://github.com/nrjl/lcm_to_ros, nicholas.lawrance@oregonstate.edu
    #######################################################################
    #
    # Source message:    .msg
    # Creation:          lun 18 feb 2019 17:14:17 CET
    #
    #######################################################################
    float64             tiempo
    float64             deriva
    float64             cabeceo
    float64             curvatura
    float64             velocidad
    float64             velocidad_consigna
                        
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new variables_control(null);
    if (msg.tiempo !== undefined) {
      resolved.tiempo = msg.tiempo;
    }
    else {
      resolved.tiempo = 0.0
    }

    if (msg.deriva !== undefined) {
      resolved.deriva = msg.deriva;
    }
    else {
      resolved.deriva = 0.0
    }

    if (msg.cabeceo !== undefined) {
      resolved.cabeceo = msg.cabeceo;
    }
    else {
      resolved.cabeceo = 0.0
    }

    if (msg.curvatura !== undefined) {
      resolved.curvatura = msg.curvatura;
    }
    else {
      resolved.curvatura = 0.0
    }

    if (msg.velocidad !== undefined) {
      resolved.velocidad = msg.velocidad;
    }
    else {
      resolved.velocidad = 0.0
    }

    if (msg.velocidad_consigna !== undefined) {
      resolved.velocidad_consigna = msg.velocidad_consigna;
    }
    else {
      resolved.velocidad_consigna = 0.0
    }

    return resolved;
    }
};

module.exports = variables_control;
