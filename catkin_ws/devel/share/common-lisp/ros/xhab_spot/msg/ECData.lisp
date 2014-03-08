; Auto-generated. Do not edit!


(cl:in-package xhab_spot-msg)


;//! \htmlinclude ECData.msg.html

(cl:defclass <ECData> (roslisp-msg-protocol:ros-message)
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
   (ec_value
    :reader ec_value
    :initarg :ec_value
    :type cl:float
    :initform 0.0))
)

(cl:defclass ECData (<ECData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ECData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ECData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name xhab_spot-msg:<ECData> is deprecated: use xhab_spot-msg:ECData instead.")))

(cl:ensure-generic-function 'spot_id-val :lambda-list '(m))
(cl:defmethod spot_id-val ((m <ECData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:spot_id-val is deprecated.  Use xhab_spot-msg:spot_id instead.")
  (spot_id m))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <ECData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:timestamp-val is deprecated.  Use xhab_spot-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'ec_value-val :lambda-list '(m))
(cl:defmethod ec_value-val ((m <ECData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:ec_value-val is deprecated.  Use xhab_spot-msg:ec_value instead.")
  (ec_value m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<ECData>)))
    "Constants for message type '<ECData>"
  '((:TARGET . ec))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'ECData)))
    "Constants for message type 'ECData"
  '((:TARGET . ec))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ECData>) ostream)
  "Serializes a message object of type '<ECData>"
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
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'ec_value))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ECData>) istream)
  "Deserializes a message object of type '<ECData>"
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
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'ec_value) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ECData>)))
  "Returns string type for a message object of type '<ECData>"
  "xhab_spot/ECData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ECData)))
  "Returns string type for a message object of type 'ECData"
  "xhab_spot/ECData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ECData>)))
  "Returns md5sum for a message object of type '<ECData>"
  "97b3308d1b5b008220b33b61897328c9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ECData)))
  "Returns md5sum for a message object of type 'ECData"
  "97b3308d1b5b008220b33b61897328c9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ECData>)))
  "Returns full string definition for message of type '<ECData>"
  (cl:format cl:nil "string spot_id~%string target = ec~%time timestamp~%float32 ec_value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ECData)))
  "Returns full string definition for message of type 'ECData"
  (cl:format cl:nil "string spot_id~%string target = ec~%time timestamp~%float32 ec_value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ECData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'spot_id))
     8
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ECData>))
  "Converts a ROS message object to a list"
  (cl:list 'ECData
    (cl:cons ':spot_id (spot_id msg))
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':ec_value (ec_value msg))
))
