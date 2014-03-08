; Auto-generated. Do not edit!


(cl:in-package xhab_spot-msg)


;//! \htmlinclude BatteryData.msg.html

(cl:defclass <BatteryData> (roslisp-msg-protocol:ros-message)
  ((spot_id
    :reader spot_id
    :initarg :spot_id
    :type cl:string
    :initform "")
   (timestamp
    :reader timestamp
    :initarg :timestamp
    :type cl:real
    :initform 0)
   (charging
    :reader charging
    :initarg :charging
    :type cl:boolean
    :initform cl:nil)
   (battery_level
    :reader battery_level
    :initarg :battery_level
    :type cl:float
    :initform 0.0))
)

(cl:defclass BatteryData (<BatteryData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BatteryData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BatteryData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name xhab_spot-msg:<BatteryData> is deprecated: use xhab_spot-msg:BatteryData instead.")))

(cl:ensure-generic-function 'spot_id-val :lambda-list '(m))
(cl:defmethod spot_id-val ((m <BatteryData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:spot_id-val is deprecated.  Use xhab_spot-msg:spot_id instead.")
  (spot_id m))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <BatteryData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:timestamp-val is deprecated.  Use xhab_spot-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'charging-val :lambda-list '(m))
(cl:defmethod charging-val ((m <BatteryData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:charging-val is deprecated.  Use xhab_spot-msg:charging instead.")
  (charging m))

(cl:ensure-generic-function 'battery_level-val :lambda-list '(m))
(cl:defmethod battery_level-val ((m <BatteryData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:battery_level-val is deprecated.  Use xhab_spot-msg:battery_level instead.")
  (battery_level m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<BatteryData>)))
    "Constants for message type '<BatteryData>"
  '((:TARGET . battery))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'BatteryData)))
    "Constants for message type 'BatteryData"
  '((:TARGET . battery))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BatteryData>) ostream)
  "Serializes a message object of type '<BatteryData>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'spot_id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'spot_id))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'timestamp)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'timestamp) (cl:floor (cl:slot-value msg 'timestamp)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'charging) 1 0)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'battery_level))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BatteryData>) istream)
  "Deserializes a message object of type '<BatteryData>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'spot_id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'spot_id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'timestamp) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:setf (cl:slot-value msg 'charging) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'battery_level) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BatteryData>)))
  "Returns string type for a message object of type '<BatteryData>"
  "xhab_spot/BatteryData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BatteryData)))
  "Returns string type for a message object of type 'BatteryData"
  "xhab_spot/BatteryData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BatteryData>)))
  "Returns md5sum for a message object of type '<BatteryData>"
  "5c7a54db53b40de9511097a6bd8b8df6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BatteryData)))
  "Returns md5sum for a message object of type 'BatteryData"
  "5c7a54db53b40de9511097a6bd8b8df6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BatteryData>)))
  "Returns full string definition for message of type '<BatteryData>"
  (cl:format cl:nil "string spot_id~%string target = battery~%time timestamp~%bool charging~%float32 battery_level~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BatteryData)))
  "Returns full string definition for message of type 'BatteryData"
  (cl:format cl:nil "string spot_id~%string target = battery~%time timestamp~%bool charging~%float32 battery_level~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BatteryData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'spot_id))
     8
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BatteryData>))
  "Converts a ROS message object to a list"
  (cl:list 'BatteryData
    (cl:cons ':spot_id (spot_id msg))
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':charging (charging msg))
    (cl:cons ':battery_level (battery_level msg))
))
