// Generated by gencpp from file motor_control/Motor2.msg
// DO NOT EDIT!


#ifndef MOTOR_CONTROL_MESSAGE_MOTOR2_H
#define MOTOR_CONTROL_MESSAGE_MOTOR2_H

#include <ros/service_traits.h>


#include <motor_control/Motor2Request.h>
#include <motor_control/Motor2Response.h>


namespace motor_control
{

struct Motor2
{

typedef Motor2Request Request;
typedef Motor2Response Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct Motor2
} // namespace motor_control


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::motor_control::Motor2 > {
  static const char* value()
  {
    return "336caa623787c2e2b9bf54c39edf8455";
  }

  static const char* value(const ::motor_control::Motor2&) { return value(); }
};

template<>
struct DataType< ::motor_control::Motor2 > {
  static const char* value()
  {
    return "motor_control/Motor2";
  }

  static const char* value(const ::motor_control::Motor2&) { return value(); }
};


// service_traits::MD5Sum< ::motor_control::Motor2Request> should match
// service_traits::MD5Sum< ::motor_control::Motor2 >
template<>
struct MD5Sum< ::motor_control::Motor2Request>
{
  static const char* value()
  {
    return MD5Sum< ::motor_control::Motor2 >::value();
  }
  static const char* value(const ::motor_control::Motor2Request&)
  {
    return value();
  }
};

// service_traits::DataType< ::motor_control::Motor2Request> should match
// service_traits::DataType< ::motor_control::Motor2 >
template<>
struct DataType< ::motor_control::Motor2Request>
{
  static const char* value()
  {
    return DataType< ::motor_control::Motor2 >::value();
  }
  static const char* value(const ::motor_control::Motor2Request&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::motor_control::Motor2Response> should match
// service_traits::MD5Sum< ::motor_control::Motor2 >
template<>
struct MD5Sum< ::motor_control::Motor2Response>
{
  static const char* value()
  {
    return MD5Sum< ::motor_control::Motor2 >::value();
  }
  static const char* value(const ::motor_control::Motor2Response&)
  {
    return value();
  }
};

// service_traits::DataType< ::motor_control::Motor2Response> should match
// service_traits::DataType< ::motor_control::Motor2 >
template<>
struct DataType< ::motor_control::Motor2Response>
{
  static const char* value()
  {
    return DataType< ::motor_control::Motor2 >::value();
  }
  static const char* value(const ::motor_control::Motor2Response&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MOTOR_CONTROL_MESSAGE_MOTOR2_H
