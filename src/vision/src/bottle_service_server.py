#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Pose, Point
from nav_msgs.msg import Odometry
from rospy_tutorials.srv import AddTwoInts, AddTwoIntsResponse
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import math

def my_callback(request):
    h = request.a
    w = request.b
    
    if(h < 10 or w <10):
        return AddTwoIntsResponse()

    global d
    if(h>w):
        d=h/float(34)
    else:
        d=w/float(34)
    
    global pose_result
    global roll, pitch, yaw
    orientation_q = pose_result.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)

    bottle_pos = Point()
    bottle_pos.x = d*math.cos(yaw)+pose_result.position.x
    bottle_pos.y = d*math.sin(yaw)+pose_result.position.y
    bottle_pos.z = 0

    print("--------------")
    print("h: " + str(h))
    print("w: " + str(w))
    print("d: " + str(d))
    print("yaw: " + str(yaw))
    print("x: " + str(pose_result.position.x))
    print("y: " + str(pose_result.position.y))
    print("bx: " + str(bottle_pos.x))
    print("by: " + str(bottle_pos.y))

    global liste
    th = 2

    for pos in liste:
        if (bottle_pos.x-th < pos.x < bottle_pos.x+th):
            if (bottle_pos.y-th < pos.y < bottle_pos.y+th):
                return AddTwoIntsResponse()

    liste.append(bottle_pos)
    pub.publish(bottle_pos)

    return AddTwoIntsResponse()

def odom_callback(msg):
    global pose_result
    pose_result = msg.pose.pose

rospy.init_node('service_server') 
my_service = rospy.Service('/bottle_service', AddTwoInts, my_callback)
pub = rospy.Publisher('/bottle', Point, queue_size=1)
pose_result = Pose()
pose_sub = rospy.Subscriber('/odom', Odometry, odom_callback)
liste = []
rospy.spin()
