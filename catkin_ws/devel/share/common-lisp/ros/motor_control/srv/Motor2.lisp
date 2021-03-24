; Auto-generated. Do not edit!


(cl:in-package motor_control-srv)


;//! \htmlinclude Motor2-request.msg.html

(cl:defclass <Motor2-request> (roslisp-msg-protocol:ros-message)
  ((order
    :reader order
    :initarg :order
    :type cl:integer
    :initform 0))
)

(cl:defclass Motor2-request (<Motor2-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Motor2-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Motor2-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name motor_control-srv:<Motor2-request> is deprecated: use motor_control-srv:Motor2-request instead.")))

(cl:ensure-generic-function 'order-val :lambda-list '(m))
(cl:defmethod order-val ((m <Motor2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motor_control-srv:order-val is deprecated.  Use motor_control-srv:order instead.")
  (order m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Motor2-request>) ostream)
  "Serializes a message object of type '<Motor2-request>"
  (cl:let* ((signed (cl:slot-value msg 'order)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Motor2-request>) istream)
  "Deserializes a message object of type '<Motor2-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'order) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Motor2-request>)))
  "Returns string type for a service object of type '<Motor2-request>"
  "motor_control/Motor2Request")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Motor2-request)))
  "Returns string type for a service object of type 'Motor2-request"
  "motor_control/Motor2Request")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Motor2-request>)))
  "Returns md5sum for a message object of type '<Motor2-request>"
  "336caa623787c2e2b9bf54c39edf8455")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Motor2-request)))
  "Returns md5sum for a message object of type 'Motor2-request"
  "336caa623787c2e2b9bf54c39edf8455")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Motor2-request>)))
  "Returns full string definition for message of type '<Motor2-request>"
  (cl:format cl:nil "int32 order~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Motor2-request)))
  "Returns full string definition for message of type 'Motor2-request"
  (cl:format cl:nil "int32 order~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Motor2-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Motor2-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Motor2-request
    (cl:cons ':order (order msg))
))
;//! \htmlinclude Motor2-response.msg.html

(cl:defclass <Motor2-response> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (position
    :reader position
    :initarg :position
    :type cl:integer
    :initform 0))
)

(cl:defclass Motor2-response (<Motor2-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Motor2-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Motor2-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name motor_control-srv:<Motor2-response> is deprecated: use motor_control-srv:Motor2-response instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <Motor2-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motor_control-srv:id-val is deprecated.  Use motor_control-srv:id instead.")
  (id m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <Motor2-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motor_control-srv:position-val is deprecated.  Use motor_control-srv:position instead.")
  (position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Motor2-response>) ostream)
  "Serializes a message object of type '<Motor2-response>"
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'position)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Motor2-response>) istream)
  "Deserializes a message object of type '<Motor2-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'position) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Motor2-response>)))
  "Returns string type for a service object of type '<Motor2-response>"
  "motor_control/Motor2Response")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Motor2-response)))
  "Returns string type for a service object of type 'Motor2-response"
  "motor_control/Motor2Response")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Motor2-response>)))
  "Returns md5sum for a message object of type '<Motor2-response>"
  "336caa623787c2e2b9bf54c39edf8455")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Motor2-response)))
  "Returns md5sum for a message object of type 'Motor2-response"
  "336caa623787c2e2b9bf54c39edf8455")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Motor2-response>)))
  "Returns full string definition for message of type '<Motor2-response>"
  (cl:format cl:nil "int32 id~%int32 position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Motor2-response)))
  "Returns full string definition for message of type 'Motor2-response"
  (cl:format cl:nil "int32 id~%int32 position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Motor2-response>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Motor2-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Motor2-response
    (cl:cons ':id (id msg))
    (cl:cons ':position (position msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Motor2)))
  'Motor2-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Motor2)))
  'Motor2-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Motor2)))
  "Returns string type for a service object of type '<Motor2>"
  "motor_control/Motor2")