; Auto-generated. Do not edit!


(cl:in-package xhab_spot-msg)


;//! \htmlinclude RotationData.msg.html

(cl:defclass <RotationData> (roslisp-msg-protocol:ros-message)
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
   (angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0)
   (currently_rotating
    :reader currently_rotating
    :initarg :currently_rotating
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass RotationData (<RotationData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RotationData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RotationData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name xhab_spot-msg:<RotationData> is deprecated: use xhab_spot-msg:RotationData instead.")))

(cl:ensure-generic-function 'spot_id-val :lambda-list '(m))
(cl:defmethod spot_id-val ((m <RotationData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:spot_id-val is deprecated.  Use xhab_spot-msg:spot_id instead.")
  (spot_id m))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <RotationData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:timestamp-val is deprecated.  Use xhab_spot-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <RotationData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:angle-val is deprecated.  Use xhab_spot-msg:angle instead.")
  (angle m))

(cl:ensure-generic-function 'currently_rotating-val :lambda-list '(m))
(cl:defmethod currently_rotating-val ((m <RotationData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:currently_rotating-val is deprecated.  Use xhab_spot-msg:currently_rotating instead.")
  (currently_rotating m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<RotationData>)))
    "Constants for message type '<RotationData>"
  '((:TARGET . rotation))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'RotationData)))
    "Constants for message type 'RotationData"
  '((:TARGET . rotation))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RotationData>) ostream)
  "Serializes a message object of type '<RotationData>"
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
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'currently_rotating) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RotationData>) istream)
  "Deserializes a message object of type '<RotationData>"
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
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'currently_rotating) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RotationData>)))
  "Returns string type for a message object of type '<RotationData>"
  "xhab_spot/RotationData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RotationData)))
  "Returns string type for a message object of type 'RotationData"
  "xhab_spot/RotationData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RotationData>)))
  "Returns md5sum for a message object of type '<RotationData>"
  "897f90a15a5b54abf331d234360ee667")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RotationData)))
  "Returns md5sum for a message object of type 'RotationData"
  "897f90a15a5b54abf331d234360ee667")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RotationData>)))
  "Returns full string definition for message of type '<RotationData>"
  (cl:format cl:nil "string spot_id~%string target = rotation~%time timestamp~%float32 angle ~%bool currently_rotating~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RotationData)))
  "Returns full string definition for message of type 'RotationData"
  (cl:format cl:nil "string spot_id~%string target = rotation~%time timestamp~%float32 angle ~%bool currently_rotating~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RotationData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'spot_id))
     8
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RotationData>))
  "Converts a ROS message object to a list"
  (cl:list 'RotationData
    (cl:cons ':spot_id (spot_id msg))
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':angle (angle msg))
    (cl:cons ':currently_rotating (currently_rotating msg))
))
