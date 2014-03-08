/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by genmsg_cpp from file /home/xhab/xhab-spot/catkin_ws/src/xhab_spot/msg/ECTask.msg
 *
 */


#ifndef XHAB_SPOT_MESSAGE_ECTASK_H
#define XHAB_SPOT_MESSAGE_ECTASK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace xhab_spot
{
template <class ContainerAllocator>
struct ECTask_
{
  typedef ECTask_<ContainerAllocator> Type;

  ECTask_()
    : spot_id()
    , timestamp()  {
    }
  ECTask_(const ContainerAllocator& _alloc)
    : spot_id(_alloc)
    , timestamp()  {
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _spot_id_type;
  _spot_id_type spot_id;

   typedef ros::Time _timestamp_type;
  _timestamp_type timestamp;


    static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  target;
 

  typedef boost::shared_ptr< ::xhab_spot::ECTask_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::xhab_spot::ECTask_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct ECTask_

typedef ::xhab_spot::ECTask_<std::allocator<void> > ECTask;

typedef boost::shared_ptr< ::xhab_spot::ECTask > ECTaskPtr;
typedef boost::shared_ptr< ::xhab_spot::ECTask const> ECTaskConstPtr;

// constants requiring out of line definition

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      ECTask_<ContainerAllocator>::target =
        
          "ec"
        
        ;
   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::xhab_spot::ECTask_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::xhab_spot::ECTask_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace xhab_spot

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/groovy/share/std_msgs/msg'], 'xhab_spot': ['/home/xhab/xhab-spot/catkin_ws/src/xhab_spot/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::xhab_spot::ECTask_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xhab_spot::ECTask_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xhab_spot::ECTask_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xhab_spot::ECTask_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xhab_spot::ECTask_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xhab_spot::ECTask_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::xhab_spot::ECTask_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3d8cec44ba2a07f268e1a1c4901b61b9";
  }

  static const char* value(const ::xhab_spot::ECTask_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3d8cec44ba2a07f2ULL;
  static const uint64_t static_value2 = 0x68e1a1c4901b61b9ULL;
};

template<class ContainerAllocator>
struct DataType< ::xhab_spot::ECTask_<ContainerAllocator> >
{
  static const char* value()
  {
    return "xhab_spot/ECTask";
  }

  static const char* value(const ::xhab_spot::ECTask_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::xhab_spot::ECTask_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string spot_id\n\
string target = ec\n\
time timestamp\n\
\n\
";
  }

  static const char* value(const ::xhab_spot::ECTask_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::xhab_spot::ECTask_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.spot_id);
      stream.next(m.timestamp);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct ECTask_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::xhab_spot::ECTask_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::xhab_spot::ECTask_<ContainerAllocator>& v)
  {
    s << indent << "spot_id: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.spot_id);
    s << indent << "timestamp: ";
    Printer<ros::Time>::stream(s, indent + "  ", v.timestamp);
  }
};

} // namespace message_operations
} // namespace ros

#endif // XHAB_SPOT_MESSAGE_ECTASK_H
