; Auto-generated. Do not edit!


(cl:in-package xhab_spot-msg)


;//! \htmlinclude CameraData.msg.html

(cl:defclass <CameraData> (roslisp-msg-protocol:ros-message)
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
   (camera_data
    :reader camera_data
    :initarg :camera_data
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass CameraData (<CameraData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CameraData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CameraData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name xhab_spot-msg:<CameraData> is deprecated: use xhab_spot-msg:CameraData instead.")))

(cl:ensure-generic-function 'spot_id-val :lambda-list '(m))
(cl:defmethod spot_id-val ((m <CameraData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:spot_id-val is deprecated.  Use xhab_spot-msg:spot_id instead.")
  (spot_id m))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <CameraData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:timestamp-val is deprecated.  Use xhab_spot-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'camera_data-val :lambda-list '(m))
(cl:defmethod camera_data-val ((m <CameraData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xhab_spot-msg:camera_data-val is deprecated.  Use xhab_spot-msg:camera_data instead.")
  (camera_data m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<CameraData>)))
    "Constants for message type '<CameraData>"
  '((:TARGET . camera)
    (:CAMERA_ENCODING . JPG))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'CameraData)))
    "Constants for message type 'CameraData"
  '((:TARGET . camera)
    (:CAMERA_ENCODING . JPG))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CameraData>) ostream)
  "Serializes a message object of type '<CameraData>"
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
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'camera_data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'camera_data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CameraData>) istream)
  "Deserializes a message object of type '<CameraData>"
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
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'camera_data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'camera_data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CameraData>)))
  "Returns string type for a message object of type '<CameraData>"
  "xhab_spot/CameraData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CameraData)))
  "Returns string type for a message object of type 'CameraData"
  "xhab_spot/CameraData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CameraData>)))
  "Returns md5sum for a message object of type '<CameraData>"
  "b81836c4ca7dbf0ece88bba1dc12e21d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CameraData)))
  "Returns md5sum for a message object of type 'CameraData"
  "b81836c4ca7dbf0ece88bba1dc12e21d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CameraData>)))
  "Returns full string definition for message of type '<CameraData>"
  (cl:format cl:nil "string spot_id~%string target = camera~%time timestamp~%string camera_encoding = JPG~%uint8[] camera_data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CameraData)))
  "Returns full string definition for message of type 'CameraData"
  (cl:format cl:nil "string spot_id~%string target = camera~%time timestamp~%string camera_encoding = JPG~%uint8[] camera_data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CameraData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'spot_id))
     8
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'camera_data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CameraData>))
  "Converts a ROS message object to a list"
  (cl:list 'CameraData
    (cl:cons ':spot_id (spot_id msg))
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':camera_data (camera_data msg))
))
