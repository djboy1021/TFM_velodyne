// Auto-generated. Do not edit!

// (in-package lcm_to_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let osm_waypoint = require('./osm_waypoint.js');

//-----------------------------------------------------------

class osm_route_result {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.id = null;
      this.n_puntos = null;
      this.puntos = null;
    }
    else {
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
      if (initObj.hasOwnProperty('n_puntos')) {
        this.n_puntos = initObj.n_puntos
      }
      else {
        this.n_puntos = 0;
      }
      if (initObj.hasOwnProperty('puntos')) {
        this.puntos = initObj.puntos
      }
      else {
        this.puntos = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type osm_route_result
    // Serialize message field [id]
    bufferOffset = _serializer.int32(obj.id, buffer, bufferOffset);
    // Serialize message field [n_puntos]
    bufferOffset = _serializer.int32(obj.n_puntos, buffer, bufferOffset);
    // Serialize message field [puntos]
    // Serialize the length for message field [puntos]
    bufferOffset = _serializer.uint32(obj.puntos.length, buffer, bufferOffset);
    obj.puntos.forEach((val) => {
      bufferOffset = osm_waypoint.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type osm_route_result
    let len;
    let data = new osm_route_result(null);
    // Deserialize message field [id]
    data.id = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [n_puntos]
    data.n_puntos = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [puntos]
    // Deserialize array length for message field [puntos]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.puntos = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.puntos[i] = osm_waypoint.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 24 * object.puntos.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'lcm_to_ros/osm_route_result';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1e17e3fc432d0f2c2a93661fa8d61a75';
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new osm_route_result(null);
    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    if (msg.n_puntos !== undefined) {
      resolved.n_puntos = msg.n_puntos;
    }
    else {
      resolved.n_puntos = 0
    }

    if (msg.puntos !== undefined) {
      resolved.puntos = new Array(msg.puntos.length);
      for (let i = 0; i < resolved.puntos.length; ++i) {
        resolved.puntos[i] = osm_waypoint.Resolve(msg.puntos[i]);
      }
    }
    else {
      resolved.puntos = []
    }

    return resolved;
    }
};

module.exports = osm_route_result;
