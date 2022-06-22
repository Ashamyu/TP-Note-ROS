#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker


publish = rospy.Publisher(topic)


rospy.init_node('marker')

marker_pub = rospy.Publisher("/vis_marker", Marker, queue_size = 2)

marker = Marker()

marker.header.frame_id = "map";
marker.header.stamp = ros.Time.now();
marker.ns = "my_marker";
marker.id = 0;
marker.type = 2;


marker.pose.position.x = 5;
marker.pose.position.y = 2;
marker.pose.position.z = 0;
marker.pose.orientation.x = 0;
marker.pose.orientation.y = 0;
marker.pose.orientation.z = 0;
marker.pose.orientation.w = 1;
marker.scale.x = 0.5;
marker.scale.y = 0.5;
marker.scale.z = 0.5;
marker.color = blue; 

while not rospy.is_shutdown():
  marker_pub.publish(marker)
  rospy.rostime.wallsleep(1.0)S
