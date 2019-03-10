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

class control_caja_orden {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.prioridad = null;
      this.valor = null;
    }
    else {
      if (initObj.hasOwnProperty('prioridad')) {
        this.prioridad = initObj.prioridad
      }
      else {
        this.prioridad = 0;
      }
      if (initObj.hasOwnProperty('valor')) {
        this.valor = initObj.valor
      }
      else {
        this.valor = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type control_caja_orden
    // Serialize message field [prioridad]
    bufferOffset = _serializer.int8(obj.prioridad, buffer, bufferOffset);
    // Serialize message field [valor]
    bufferOffset = _serializer.float64(obj.valor, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type control_caja_orden
    let len;
    let data = new control_caja_orden(null);
    // Deserialize message field [prioridad]
    data.prioridad = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [valor]
    data.valor = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'lcm_to_ros/control_caja_orden';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fccc8a5a7c3d9b41585ac5dee68ebfb2';
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
    int8                prioridad
    float64             valor
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new control_caja_orden(null);
    if (msg.prioridad !== undefined) {
      resolved.prioridad = msg.prioridad;
    }
    else {
      resolved.prioridad = 0
    }

    if (msg.valor !== undefined) {
      resolved.valor = msg.valor;
    }
    else {
      resolved.valor = 0.0
    }

    return resolved;
    }
};

module.exports = control_caja_orden;
