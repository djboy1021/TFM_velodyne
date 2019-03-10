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

class can_modulo_orden {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ValorAnalog = null;
      this.IdModulo = null;
      this.Orden = null;
      this.ValorDigital = null;
    }
    else {
      if (initObj.hasOwnProperty('ValorAnalog')) {
        this.ValorAnalog = initObj.ValorAnalog
      }
      else {
        this.ValorAnalog = 0.0;
      }
      if (initObj.hasOwnProperty('IdModulo')) {
        this.IdModulo = initObj.IdModulo
      }
      else {
        this.IdModulo = 0;
      }
      if (initObj.hasOwnProperty('Orden')) {
        this.Orden = initObj.Orden
      }
      else {
        this.Orden = 0;
      }
      if (initObj.hasOwnProperty('ValorDigital')) {
        this.ValorDigital = initObj.ValorDigital
      }
      else {
        this.ValorDigital = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type can_modulo_orden
    // Serialize message field [ValorAnalog]
    bufferOffset = _serializer.float64(obj.ValorAnalog, buffer, bufferOffset);
    // Serialize message field [IdModulo]
    bufferOffset = _serializer.byte(obj.IdModulo, buffer, bufferOffset);
    // Serialize message field [Orden]
    bufferOffset = _serializer.byte(obj.Orden, buffer, bufferOffset);
    // Serialize message field [ValorDigital]
    bufferOffset = _serializer.byte(obj.ValorDigital, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type can_modulo_orden
    let len;
    let data = new can_modulo_orden(null);
    // Deserialize message field [ValorAnalog]
    data.ValorAnalog = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [IdModulo]
    data.IdModulo = _deserializer.byte(buffer, bufferOffset);
    // Deserialize message field [Orden]
    data.Orden = _deserializer.byte(buffer, bufferOffset);
    // Deserialize message field [ValorDigital]
    data.ValorDigital = _deserializer.byte(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 11;
  }

  static datatype() {
    // Returns string type for a message object
    return 'lcm_to_ros/can_modulo_orden';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a74929a645129209cfc4d5dd7332d340';
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
    # Creation:          lun 18 feb 2019 17:14:16 CET
    #
    #######################################################################
    float64             ValorAnalog
    byte                IdModulo
    byte                Orden
    byte                ValorDigital
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new can_modulo_orden(null);
    if (msg.ValorAnalog !== undefined) {
      resolved.ValorAnalog = msg.ValorAnalog;
    }
    else {
      resolved.ValorAnalog = 0.0
    }

    if (msg.IdModulo !== undefined) {
      resolved.IdModulo = msg.IdModulo;
    }
    else {
      resolved.IdModulo = 0
    }

    if (msg.Orden !== undefined) {
      resolved.Orden = msg.Orden;
    }
    else {
      resolved.Orden = 0
    }

    if (msg.ValorDigital !== undefined) {
      resolved.ValorDigital = msg.ValorDigital;
    }
    else {
      resolved.ValorDigital = 0
    }

    return resolved;
    }
};

module.exports = can_modulo_orden;
