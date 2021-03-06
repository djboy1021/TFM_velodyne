// Generated by gencpp from file lcm_to_ros/osm_route_result.msg
// DO NOT EDIT!


#ifndef LCM_TO_ROS_MESSAGE_OSM_ROUTE_RESULT_H
#define LCM_TO_ROS_MESSAGE_OSM_ROUTE_RESULT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <lcm_to_ros/osm_waypoint.h>

namespace lcm_to_ros
{
template <class ContainerAllocator>
struct osm_route_result_
{
  typedef osm_route_result_<ContainerAllocator> Type;

  osm_route_result_()
    : id(0)
    , n_puntos(0)
    , puntos()  {
    }
  osm_route_result_(const ContainerAllocator& _alloc)
    : id(0)
    , n_puntos(0)
    , puntos(_alloc)  {
  (void)_alloc;
    }



   typedef int32_t _id_type;
  _id_type id;

   typedef int32_t _n_puntos_type;
  _n_puntos_type n_puntos;

   typedef std::vector< ::lcm_to_ros::osm_waypoint_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::lcm_to_ros::osm_waypoint_<ContainerAllocator> >::other >  _puntos_type;
  _puntos_type puntos;





  typedef boost::shared_ptr< ::lcm_to_ros::osm_route_result_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::lcm_to_ros::osm_route_result_<ContainerAllocator> const> ConstPtr;

}; // struct osm_route_result_

typedef ::lcm_to_ros::osm_route_result_<std::allocator<void> > osm_route_result;

typedef boost::shared_ptr< ::lcm_to_ros::osm_route_result > osm_route_resultPtr;
typedef boost::shared_ptr< ::lcm_to_ros::osm_route_result const> osm_route_resultConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::lcm_to_ros::osm_route_result_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::lcm_to_ros::osm_route_result_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace lcm_to_ros

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'lcm_to_ros': ['/home/alberto/workspaces/workspace14diciembre/src/lcm_to_ros/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::lcm_to_ros::osm_route_result_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lcm_to_ros::osm_route_result_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lcm_to_ros::osm_route_result_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lcm_to_ros::osm_route_result_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lcm_to_ros::osm_route_result_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lcm_to_ros::osm_route_result_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::lcm_to_ros::osm_route_result_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1e17e3fc432d0f2c2a93661fa8d61a75";
  }

  static const char* value(const ::lcm_to_ros::osm_route_result_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1e17e3fc432d0f2cULL;
  static const uint64_t static_value2 = 0x2a93661fa8d61a75ULL;
};

template<class ContainerAllocator>
struct DataType< ::lcm_to_ros::osm_route_result_<ContainerAllocator> >
{
  static const char* value()
  {
    return "lcm_to_ros/osm_route_result";
  }

  static const char* value(const ::lcm_to_ros::osm_route_result_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::lcm_to_ros::osm_route_result_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#######################################################################\n\
# This message was automatically generated by the lcm_to_ros package\n\
# https://github.com/nrjl/lcm_to_ros, nicholas.lawrance@oregonstate.edu\n\
#######################################################################\n\
#\n\
# Source message:    .msg\n\
# Creation:          lun 18 feb 2019 17:14:17 CET\n\
#\n\
#######################################################################\n\
int32               id\n\
int32               n_puntos\n\
osm_waypoint[]      puntos\n\
\n\
================================================================================\n\
MSG: lcm_to_ros/osm_waypoint\n\
#######################################################################\n\
# This message was automatically generated by the lcm_to_ros package\n\
# https://github.com/nrjl/lcm_to_ros, nicholas.lawrance@oregonstate.edu\n\
#######################################################################\n\
#\n\
# Source message:    .msg\n\
# Creation:          lun 18 feb 2019 17:14:17 CET\n\
#\n\
#######################################################################\n\
float64             latitud\n\
float64             longitud\n\
float64             orientacion\n\
";
  }

  static const char* value(const ::lcm_to_ros::osm_route_result_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::lcm_to_ros::osm_route_result_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.n_puntos);
      stream.next(m.puntos);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct osm_route_result_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::lcm_to_ros::osm_route_result_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::lcm_to_ros::osm_route_result_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.id);
    s << indent << "n_puntos: ";
    Printer<int32_t>::stream(s, indent + "  ", v.n_puntos);
    s << indent << "puntos[]" << std::endl;
    for (size_t i = 0; i < v.puntos.size(); ++i)
    {
      s << indent << "  puntos[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::lcm_to_ros::osm_waypoint_<ContainerAllocator> >::stream(s, indent + "    ", v.puntos[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // LCM_TO_ROS_MESSAGE_OSM_ROUTE_RESULT_H
