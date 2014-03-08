; Auto-generated. Do not edit!


(cl:in-package xhab_spot-msg)


;//! \htmlinclude LightsTask.msg.html

(cl:defclass <LightsTask> (roslisp-msg-protocol:ros-message)
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
   (brightness
    :reader brightness
    :initarg :brightness
    :type cl:float
    :initform 0.0)
   (whites_on
    :reader whites_on
    :initarg :whites_on
    :type cl:boolean
    :initform cl:nil)
   (reds_on
    :reader reds_on
    :initarg :reds_on
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass LightsTask (<LightsTask>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LightsTask>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LightsTask)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name xhab_spot-msg:<LightsTask> is deprecated: use xhab_spot-msg:LightsTask instead.")))

(cl:ensure-generic-function 'spot_id-val :lambda-list '(m))
(cl:defmethod spot_id-val ((m <LightsTask>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:spot_id-val is deprecated.  Use xhab_spot-msg:spot_id instead.")
  (spot_id m))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <LightsTask>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:timestamp-val is deprecated.  Use xhab_spot-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'brightness-val :lambda-list '(m))
(cl:defmethod brightness-val ((m <LightsTask>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:brightness-val is deprecated.  Use xhab_spot-msg:brightness instead.")
  (brightness m))

(cl:ensure-generic-function 'whites_on-val :lambda-list '(m))
(cl:defmethod whites_on-val ((m <LightsTask>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:whites_on-val is deprecated.  Use xhab_spot-msg:whites_on instead.")
  (whites_on m))

(cl:ensure-generic-function 'reds_on-val :lambda-list '(m))
(cl:defmethod reds_on-val ((m <LightsTask>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:reds_on-val is deprecated.  Use xhab_spot-msg:reds_on instead.")
  (reds_on m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<LightsTask>)))
    "Constants for message type '<LightsTask>"
  '((:TARGET . lights))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'LightsTask)))
    "Constants for message type 'LightsTask"
  '((:TARGET . lights))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LightsTask>) ostream)
  "Serializes a message object of type '<LightsTask>"
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
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'brightness))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'whites_on) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'reds_on) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LightsTask>) istream)
  "Deserializes a message object of type '<LightsTask>"
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
    (cl:setf (cl:slot-value msg 'brightness) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'whites_on) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'reds_on) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LightsTask>)))
  "Returns string type for a message object of type '<LightsTask>"
  "xhab_spot/LightsTask")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LightsTask)))
  "Returns string type for a message object of type 'LightsTask"
  "xhab_spot/LightsTask")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LightsTask>)))
  "Returns md5sum for a message object of type '<LightsTask>"
  "dc28d7a3fa71532943c24e8e4d0eacc8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LightsTask)))
  "Returns md5sum for a message object of type 'LightsTask"
  "dc28d7a3fa71532943c24e8e4d0eacc8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LightsTask>)))
  "Returns full string definition for message of type '<LightsTask>"
  (cl:format cl:nil "string spot_id~%string target = lights~%time timestamp~%float32 brightness~%bool whites_on~%bool reds_on~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LightsTask)))
  "Returns full string definition for message of type 'LightsTask"
  (cl:format cl:nil "string spot_id~%string target = lights~%time timestamp~%float32 brightness~%bool whites_on~%bool reds_on~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LightsTask>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'spot_id))
     8
     4
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LightsTask>))
  "Converts a ROS message object to a list"
  (cl:list 'LightsTask
    (cl:cons ':spot_id (spot_id msg))
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':brightness (brightness msg))
    (cl:cons ':whites_on (whites_on msg))
    (cl:cons ':reds_on (reds_on msg))
))
