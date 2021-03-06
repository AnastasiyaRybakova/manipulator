# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from open_manipulator_msgs/GetKinematicsPoseRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetKinematicsPoseRequest(genpy.Message):
  _md5sum = "14dd5674451c0fe6eacac0ded7197f30"
  _type = "open_manipulator_msgs/GetKinematicsPoseRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string planning_group
string end_effector_name
"""
  __slots__ = ['planning_group','end_effector_name']
  _slot_types = ['string','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       planning_group,end_effector_name

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetKinematicsPoseRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.planning_group is None:
        self.planning_group = ''
      if self.end_effector_name is None:
        self.end_effector_name = ''
    else:
      self.planning_group = ''
      self.end_effector_name = ''

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
      _x = self.planning_group
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.end_effector_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planning_group = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.planning_group = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.end_effector_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.end_effector_name = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.planning_group
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.end_effector_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planning_group = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.planning_group = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.end_effector_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.end_effector_name = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from open_manipulator_msgs/GetKinematicsPoseResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import open_manipulator_msgs.msg
import std_msgs.msg

class GetKinematicsPoseResponse(genpy.Message):
  _md5sum = "3b64b73433e2775c9c4b7e1a00dd6995"
  _type = "open_manipulator_msgs/GetKinematicsPoseResponse"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
KinematicsPose kinematics_pose


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: open_manipulator_msgs/KinematicsPose
geometry_msgs/Pose  pose
float64    max_accelerations_scaling_factor
float64    max_velocity_scaling_factor
float64    tolerance

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['header','kinematics_pose']
  _slot_types = ['std_msgs/Header','open_manipulator_msgs/KinematicsPose']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,kinematics_pose

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetKinematicsPoseResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.kinematics_pose is None:
        self.kinematics_pose = open_manipulator_msgs.msg.KinematicsPose()
    else:
      self.header = std_msgs.msg.Header()
      self.kinematics_pose = open_manipulator_msgs.msg.KinematicsPose()

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_10d().pack(_x.kinematics_pose.pose.position.x, _x.kinematics_pose.pose.position.y, _x.kinematics_pose.pose.position.z, _x.kinematics_pose.pose.orientation.x, _x.kinematics_pose.pose.orientation.y, _x.kinematics_pose.pose.orientation.z, _x.kinematics_pose.pose.orientation.w, _x.kinematics_pose.max_accelerations_scaling_factor, _x.kinematics_pose.max_velocity_scaling_factor, _x.kinematics_pose.tolerance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.kinematics_pose is None:
        self.kinematics_pose = open_manipulator_msgs.msg.KinematicsPose()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 80
      (_x.kinematics_pose.pose.position.x, _x.kinematics_pose.pose.position.y, _x.kinematics_pose.pose.position.z, _x.kinematics_pose.pose.orientation.x, _x.kinematics_pose.pose.orientation.y, _x.kinematics_pose.pose.orientation.z, _x.kinematics_pose.pose.orientation.w, _x.kinematics_pose.max_accelerations_scaling_factor, _x.kinematics_pose.max_velocity_scaling_factor, _x.kinematics_pose.tolerance,) = _get_struct_10d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_10d().pack(_x.kinematics_pose.pose.position.x, _x.kinematics_pose.pose.position.y, _x.kinematics_pose.pose.position.z, _x.kinematics_pose.pose.orientation.x, _x.kinematics_pose.pose.orientation.y, _x.kinematics_pose.pose.orientation.z, _x.kinematics_pose.pose.orientation.w, _x.kinematics_pose.max_accelerations_scaling_factor, _x.kinematics_pose.max_velocity_scaling_factor, _x.kinematics_pose.tolerance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.kinematics_pose is None:
        self.kinematics_pose = open_manipulator_msgs.msg.KinematicsPose()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 80
      (_x.kinematics_pose.pose.position.x, _x.kinematics_pose.pose.position.y, _x.kinematics_pose.pose.position.z, _x.kinematics_pose.pose.orientation.x, _x.kinematics_pose.pose.orientation.y, _x.kinematics_pose.pose.orientation.z, _x.kinematics_pose.pose.orientation.w, _x.kinematics_pose.max_accelerations_scaling_factor, _x.kinematics_pose.max_velocity_scaling_factor, _x.kinematics_pose.tolerance,) = _get_struct_10d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_10d = None
def _get_struct_10d():
    global _struct_10d
    if _struct_10d is None:
        _struct_10d = struct.Struct("<10d")
    return _struct_10d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
class GetKinematicsPose(object):
  _type          = 'open_manipulator_msgs/GetKinematicsPose'
  _md5sum = '2fe60b9f4a4b683c14e60a854bb9e0e1'
  _request_class  = GetKinematicsPoseRequest
  _response_class = GetKinematicsPoseResponse
