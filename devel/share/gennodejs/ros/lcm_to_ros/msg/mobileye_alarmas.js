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

class mobileye_alarmas {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.timestamp_sec = null;
      this.timestamp_nsec = null;
      this.flags = null;
      this.headway = null;
      this.warningLevel = null;
    }
    else {
      if (initObj.hasOwnProperty('timestamp_sec')) {
        this.timestamp_sec = initObj.timestamp_sec
      }
      else {
        this.timestamp_sec = 0;
      }
      if (initObj.hasOwnProperty('timestamp_nsec')) {
        this.timestamp_nsec = initObj.timestamp_nsec
      }
      else {
        this.timestamp_nsec = 0;
      }
      if (initObj.hasOwnProperty('flags')) {
        this.flags = initObj.flags
      }
      else {
        this.flags = 0;
      }
      if (initObj.hasOwnProperty('headway')) {
        this.headway = initObj.headway
      }
      else {
        this.headway = 0.0;
      }
      if (initObj.hasOwnProperty('warningLevel')) {
        this.warningLevel = initObj.warningLevel
      }
      else {
        this.warningLevel = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type mobileye_alarmas
    // Serialize message field [timestamp_sec]
    bufferOffset = _serializer.int32(obj.timestamp_sec, buffer, bufferOffset);
    // Serialize message field [timestamp_nsec]
    bufferOffset = _serializer.int32(obj.timestamp_nsec, buffer, bufferOffset);
    // Serialize message field [flags]
    bufferOffset = _serializer.int16(obj.flags, buffer, bufferOffset);
    // Serialize message field [headway]
    bufferOffset = _serializer.float32(obj.headway, buffer, bufferOffset);
    // Serialize message field [warningLevel]
    bufferOffset = _serializer.byte(obj.warningLevel, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type mobileye_alarmas
    let len;
    let data = new mobileye_alarmas(null);
    // Deserialize message field [timestamp_sec]
    data.timestamp_sec = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [timestamp_nsec]
    data.timestamp_nsec = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [flags]
    data.flags = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [headway]
    data.headway = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [warningLevel]
    data.warningLevel = _deserializer.byte(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 15;
  }

  static datatype() {
    // Returns string type for a message object
    return 'lcm_to_ros/mobileye_alarmas';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '275230c90d76753bca3bff6115559522';
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
    int32               timestamp_sec
    int32               timestamp_nsec
    int16               flags
    float32             headway
    byte                warningLevel
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new mobileye_alarmas(null);
    if (msg.timestamp_sec !== undefined) {
      resolved.timestamp_sec = msg.timestamp_sec;
    }
    else {
      resolved.timestamp_sec = 0
    }

    if (msg.timestamp_nsec !== undefined) {
      resolved.timestamp_nsec = msg.timestamp_nsec;
    }
    else {
      resolved.timestamp_nsec = 0
    }

    if (msg.flags !== undefined) {
      resolved.flags = msg.flags;
    }
    else {
      resolved.flags = 0
    }

    if (msg.headway !== undefined) {
      resolved.headway = msg.headway;
    }
    else {
      resolved.headway = 0.0
    }

    if (msg.warningLevel !== undefined) {
      resolved.warningLevel = msg.warningLevel;
    }
    else {
      resolved.warningLevel = 0
    }

    return resolved;
    }
};

module.exports = mobileye_alarmas;
