"""
Date: 08/26/2021

Purpose: This script creates an ArmController and uses it to command the arm's
joint positions and gripper.

Try changing the target position to see what the arm does!

"""

import sys
import rospy
import numpy as np
from math import pi

from core.interfaces import ArmController

rospy.init_node('demo')

arm = ArmController()
arm.set_arm_speed(0.2)

arm.close_gripper()

q = arm.neutral_position()
arm.safe_move_to_position(q)
arm.open_gripper()

#q = np.array([0,0 ,0,0,0,0,0])
q = np.array([ pi/2, pi/2,  0, -0.07,     0,    0,    0 ]),
#q = np.array([ 0,    0,  2.89, -pi/2,   2.7, pi/2, pi/4 ]),
#q = np.array([ 0,-pi/4,     0,-3*pi/4,  2.7, pi/2, pi/4 ]),
# TODO: try changing this!
arm.safe_move_to_position(q)
arm.close_gripper()
