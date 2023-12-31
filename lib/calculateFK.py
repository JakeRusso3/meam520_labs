import numpy as np
import math
from math import pi, cos, sin

class FK():

    def __init__(self):

        # TODO: you may want to define geometric parameters here that will be
        # useful in computing the forward kinematics. The data you will need
        # is provided in the lab handout

        pass
        
    def dh_to_matrix(self, th, d, r, al):
        return np.array([
            [cos(th), -sin(th)*cos(al), sin(th)*sin(al), r*cos(th)],
            [sin(th), cos(th)*cos(al), -cos(th)*sin(al), r*sin(th)],
            [0, sin(al), cos(al), d],
            [0, 0, 0, 1]
        ])
    

    def forward(self, q):
        """
        INPUT:
        q - 1x7 vector of joint angles [q0, q1, q2, q3, q4, q5, q6]

        OUTPUTS:
        jointPositions -8 x 3 matrix, where each row corresponds to a rotational joint of the robot or end effector
                  Each row contains the [x,y,z] coordinates in the world frame of the respective joint's center in meters.
                  The base of the robot is located at [0,0,0].
        T0e       - a 4 x 4 homogeneous transformation matrix,
                  representing the end effector frame expressed in the
                  world frame
        """
        th1 = q[0]
        th2 = q[1]
        th3 = q[2]
        th4 = q[3]
        th5 = q[4]
        th6 = q[5]
        th7 = q[6]
        l1 = 0.141
        l2 = 0.192
        l3 = 0.195
        l4 = 0.0825
        l5 = 0.121
        l6 = 0.125
        l7 = 0.259
        l8 = 0.088
        l9 = 0.051
        l10 = 0.159
        l11 = 0.015
        
        H01 = self.dh_to_matrix(th1, l1+l2, 0, -pi/2)
        H12 = self.dh_to_matrix(th2, 0, 0, pi/2)
        H23 = self.dh_to_matrix(th3, l3+l5, l4, pi/2)
        H34 = self.dh_to_matrix(th4 + pi, 0, l4, pi/2)
        H45 = self.dh_to_matrix(th5, l6+l7, 0, -pi/2)  
        H56 = self.dh_to_matrix(th6 - pi, 0, l8, pi/2)
        H67 = self.dh_to_matrix(th7-pi/4, l9+l10, 0, 0)

        T01 = H01
        T02 = np.dot(T01, H12)
        T03 = np.dot(T02, H23)
        T04 = np.dot(T03, H34)
        T05 = np.dot(T04, H45)
        T06 = np.dot(T05, H56)
        T07 = np.dot(T06, H67)
        
        P1 = np.dot(T01, np.array([0,l2,0,1]))
        P2 = np.dot(T02, np.array([0,0,0,1]))
        P3 = np.dot(T03, np.array([-l4, -l5, 0, 1]))
        P4 = np.dot(T04, np.array([-l4, 0, 0, 1]))
        P5 = np.dot(T05, np.array([0, l7, 0, 1]))
        P6 = np.dot(T06, np.array([-l8, -l11, 0, 1]))
        P7 = np.dot(T07, np.array([0,0,-l10,1]))
        P8 = np.dot(T07, np.array([0,0,0,1]))
                    

        jointPositions = np.array([
            
            [P1[0], P1[1], P1[2]],
            [P2[0], P2[1], P2[2]],
            [P3[0], P3[1], P3[2]],
            [P4[0], P4[1], P4[2]],
            [P5[0], P5[1], P5[2]],
            [P6[0], P6[1], P6[2]],
            [P7[0], P7[1], P7[2]],
            [P8[0], P8[1], P8[2]]
            
        ])
        T0e =  np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(H01, H12),H23), H34), 
                      H45), H56), H67)

        # Your code ends here

        return jointPositions, T0e

    # feel free to define additional helper methods to modularize your solution for lab 1
    def get_T(self, q):
        th1 = q[0]
        th2 = q[1]
        th3 = q[2]
        th4 = q[3]
        th5 = q[4]
        th6 = q[5]
        th7 = q[6]
        l1 = 0.141
        l2 = 0.192
        l3 = 0.195
        l4 = 0.0825
        l5 = 0.121
        l6 = 0.125
        l7 = 0.259
        l8 = 0.088
        l9 = 0.051
        l10 = 0.159
        l11 = 0.015
        H01 = self.dh_to_matrix(th1, l1+l2, 0, -pi/2)
        H12 = self.dh_to_matrix(th2, 0, 0, pi/2)
        H23 = self.dh_to_matrix(th3, l3+l5, l4, pi/2)
        H34 = self.dh_to_matrix(th4 + pi, 0, l4, pi/2)
        H45 = self.dh_to_matrix(th5, l6+l7, 0, -pi/2)  
        H56 = self.dh_to_matrix(th6 - pi, 0, l8, pi/2)
        H67 = self.dh_to_matrix(th7-pi/4, l9+l10, 0, 0)

        T01 = H01
        T02 = np.dot(T01, H12)
        T03 = np.dot(T02, H23)
        T04 = np.dot(T03, H34)
        T05 = np.dot(T04, H45)
        T06 = np.dot(T05, H56)
        T07 = np.dot(T06, H67)

        All_Ts = [T01,T02,T03,T04,T05,T06,T07]
        return All_Ts
        
    # This code is for Lab 2, you can ignore it ofr Lab 1
    def get_axis_of_rotation(self, q):
        """
        INPUT:
        q - 1x7 vector of joint angles [q0, q1, q2, q3, q4, q5, q6]

        OUTPUTS:
        axis_of_rotation_list: - 3x7 np array of unit vectors describing the axis of rotation for each joint in the
                                 world frame

        """


        return()
    
    def compute_Ai(self, q):
        """
        INPUT:
        q - 1x7 vector of joint angles [q0, q1, q2, q3, q4, q5, q6]

        OUTPUTS:
        Ai: - 4x4 list of np array of homogenous transformations describing the FK of the robot. Transformations are not
              necessarily located at the joint locations
        """
        # STUDENT CODE HERE: This is a function needed by lab 2

        return()
    
if __name__ == "__main__":

    fk = FK()

    # matches figure in the handout
    q = np.array([0,0,0,-pi/2,0,pi/2,pi/4])

    joint_positions, T0e = fk.forward(q)
    
    print("Joint Positions:\n",joint_positions)
    print("End Effector Pose:\n",T0e)
