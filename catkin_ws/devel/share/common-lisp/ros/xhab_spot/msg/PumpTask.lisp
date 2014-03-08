; Auto-generated. Do not edit!


(cl:in-package xhab_spot-msg)


;//! \htmlinclude PumpTask.msg.html

(cl:defclass <PumpTask> (roslisp-msg-protocol:ros-message)
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
   (on
    :reader on
    :initarg :on
    :type cl:boolean
    :initform cl:nil)
   (temporary_disable
    :reader temporary_disable
    :initarg :temporary_disable
    :type cl:boolean
    :initform cl:nil)
   (disable_duration
    :reader disable_duration
    :initarg :disable_duration
    :type cl:fixnum
    :initform 0))
)

(cl:defclass PumpTask (<PumpTask>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PumpTask>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PumpTask)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name xhab_spot-msg:<PumpTask> is deprecated: use xhab_spot-msg:PumpTask instead.")))

(cl:ensure-generic-function 'spot_id-val :lambda-list '(m))
(cl:defmethod spot_id-val ((m <PumpTask>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:spot_id-val is deprecated.  Use xhab_spot-msg:spot_id instead.")
  (spot_id m))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <PumpTask>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:timestamp-val is deprecated.  Use xhab_spot-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'on-val :lambda-list '(m))
(cl:defmethod on-val ((m <PumpTask>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:on-val is deprecated.  Use xhab_spot-msg:on instead.")
  (on m))

(cl:ensure-generic-function 'temporary_disable-val :lambda-list '(m))
(cl:defmethod temporary_disable-val ((m <PumpTask>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:temporary_disable-val is deprecated.  Use xhab_spot-msg:temporary_disable instead.")
  (temporary_disable m))

(cl:ensure-generic-function 'disable_duration-val :lambda-list '(m))
(cl:defmethod disable_duration-val ((m <PumpTask>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:disable_duration-val is deprecated.  Use xhab_spot-msg:disable_duration instead.")
  (disable_duration m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<PumpTask>)))
    "Constants for message type '<PumpTask>"
  '((:TARGET . pump))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'PumpTask)))
    "Constants for message type 'PumpTask"
  '((:TARGET . pump))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PumpTask>) ostream)
  "Serializes a message object of type '<PumpTask>"
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
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'on) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'temporary_disable) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'disable_duration)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PumpTask>) istream)
  "Deserializes a message object of type '<PumpTask>"
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
    (cl:setf (cl:slot-value msg 'on) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'temporary_disable) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'disable_duration)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PumpTask>)))
  "Returns string type for a message object of type '<PumpTask>"
  "xhab_spot/PumpTask")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PumpTask)))
  "Returns string type for a message object of type 'PumpTask"
  "xhab_spot/PumpTask")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PumpTask>)))
  "Returns md5sum for a message object of type '<PumpTask>"
  "55dbe0a6f790ba80793049cb52c83d09")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PumpTask)))
  "Returns md5sum for a message object of type 'PumpTask"
  "55dbe0a6f790ba80793049cb52c83d09")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PumpTask>)))
  "Returns full string definition for message of type '<PumpTask>"
  (cl:format cl:nil "string spot_id~%string target = pump~%time timestamp~%bool on~%bool temporary_disable~%uint8 disable_duration~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PumpTask)))
  "Returns full string definition for message of type 'PumpTask"
  (cl:format cl:nil "string spot_id~%string target = pump~%time timestamp~%bool on~%bool temporary_disable~%uint8 disable_duration~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PumpTask>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'spot_id))
     8
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PumpTask>))
  "Converts a ROS message object to a list"
  (cl:list 'PumpTask
    (cl:cons ':spot_id (spot_id msg))
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':on (on msg))
    (cl:cons ':temporary_disable (temporary_disable msg))
    (cl:cons ':disable_duration (disable_duration msg))
))
