; Auto-generated. Do not edit!


(cl:in-package xhab_spot-msg)


;//! \htmlinclude CurtainData.msg.html

(cl:defclass <CurtainData> (roslisp-msg-protocol:ros-message)
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
   (open
    :reader open
    :initarg :open
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass CurtainData (<CurtainData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CurtainData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CurtainData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name xhab_spot-msg:<CurtainData> is deprecated: use xhab_spot-msg:CurtainData instead.")))

(cl:ensure-generic-function 'spot_id-val :lambda-list '(m))
(cl:defmethod spot_id-val ((m <CurtainData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:spot_id-val is deprecated.  Use xhab_spot-msg:spot_id instead.")
  (spot_id m))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <CurtainData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:timestamp-val is deprecated.  Use xhab_spot-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'open-val :lambda-list '(m))
(cl:defmethod open-val ((m <CurtainData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:open-val is deprecated.  Use xhab_spot-msg:open instead.")
  (open m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<CurtainData>)))
    "Constants for message type '<CurtainData>"
  '((:TARGET . curtain))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'CurtainData)))
    "Constants for message type 'CurtainData"
  '((:TARGET . curtain))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CurtainData>) ostream)
  "Serializes a message object of type '<CurtainData>"
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
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'open) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CurtainData>) istream)
  "Deserializes a message object of type '<CurtainData>"
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
    (cl:setf (cl:slot-value msg 'open) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CurtainData>)))
  "Returns string type for a message object of type '<CurtainData>"
  "xhab_spot/CurtainData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CurtainData)))
  "Returns string type for a message object of type 'CurtainData"
  "xhab_spot/CurtainData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CurtainData>)))
  "Returns md5sum for a message object of type '<CurtainData>"
  "ad6a16326bbf0f6b622e8e476cfc47e2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CurtainData)))
  "Returns md5sum for a message object of type 'CurtainData"
  "ad6a16326bbf0f6b622e8e476cfc47e2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CurtainData>)))
  "Returns full string definition for message of type '<CurtainData>"
  (cl:format cl:nil "string spot_id~%string target = curtain~%time timestamp~%bool open~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CurtainData)))
  "Returns full string definition for message of type 'CurtainData"
  (cl:format cl:nil "string spot_id~%string target = curtain~%time timestamp~%bool open~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CurtainData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'spot_id))
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CurtainData>))
  "Converts a ROS message object to a list"
  (cl:list 'CurtainData
    (cl:cons ':spot_id (spot_id msg))
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':open (open msg))
))
