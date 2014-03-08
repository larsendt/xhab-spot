; Auto-generated. Do not edit!


(cl:in-package xhab_spot-msg)


;//! \htmlinclude WaterData.msg.html

(cl:defclass <WaterData> (roslisp-msg-protocol:ros-message)
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
   (water_level
    :reader water_level
    :initarg :water_level
    :type cl:float
    :initform 0.0))
)

(cl:defclass WaterData (<WaterData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WaterData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WaterData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name xhab_spot-msg:<WaterData> is deprecated: use xhab_spot-msg:WaterData instead.")))

(cl:ensure-generic-function 'spot_id-val :lambda-list '(m))
(cl:defmethod spot_id-val ((m <WaterData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:spot_id-val is deprecated.  Use xhab_spot-msg:spot_id instead.")
  (spot_id m))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <WaterData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:timestamp-val is deprecated.  Use xhab_spot-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'water_level-val :lambda-list '(m))
(cl:defmethod water_level-val ((m <WaterData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:water_level-val is deprecated.  Use xhab_spot-msg:water_level instead.")
  (water_level m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<WaterData>)))
    "Constants for message type '<WaterData>"
  '((:TARGET . water))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'WaterData)))
    "Constants for message type 'WaterData"
  '((:TARGET . water))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WaterData>) ostream)
  "Serializes a message object of type '<WaterData>"
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
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'water_level))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WaterData>) istream)
  "Deserializes a message object of type '<WaterData>"
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
    (cl:setf (cl:slot-value msg 'water_level) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WaterData>)))
  "Returns string type for a message object of type '<WaterData>"
  "xhab_spot/WaterData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WaterData)))
  "Returns string type for a message object of type 'WaterData"
  "xhab_spot/WaterData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WaterData>)))
  "Returns md5sum for a message object of type '<WaterData>"
  "d1b8bf6948fe098a51dc5974a5ca56f5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WaterData)))
  "Returns md5sum for a message object of type 'WaterData"
  "d1b8bf6948fe098a51dc5974a5ca56f5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WaterData>)))
  "Returns full string definition for message of type '<WaterData>"
  (cl:format cl:nil "string spot_id~%string target = water~%time timestamp~%float32 water_level~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WaterData)))
  "Returns full string definition for message of type 'WaterData"
  (cl:format cl:nil "string spot_id~%string target = water~%time timestamp~%float32 water_level~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WaterData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'spot_id))
     8
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WaterData>))
  "Converts a ROS message object to a list"
  (cl:list 'WaterData
    (cl:cons ':spot_id (spot_id msg))
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':water_level (water_level msg))
))
