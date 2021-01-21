#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
import matplotlib.pyplot as plt
from std_srvs.srv import Empty
from geometry_msgs.msg import Point
from rospy_tutorials.srv import AddTwoInts, AddTwoIntsResponse


class LoadFeature(object):

    def __init__(self):
    
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.camera_callback)
        self.bridge_object = CvBridge()
        self.bottle_found = rospy.ServiceProxy('/bottle_service', AddTwoInts)

    def camera_callback(self,data):
        try:
            # We select bgr8 because its the OpenCV encoding by default
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)
        

        image_1 = cv2.imread('/home/user/catkin_ws/src/vision/ressources/coke.png',1)
        image_2 = cv_image
        
        image_1 = cv2.resize(image_1,(300,200))
        image_2 = cv2.resize(image_2,(300,200))

        # Creating a red mask to only see the red
        min_red = np.array([60,0,0])
        max_red = np.array([255,200,200])
        hsv = cv2.cvtColor(image_2, cv2.COLOR_BGR2HSV)
        mask_r = cv2.inRange(hsv, min_red, max_red)

        #Initialize the ORB Feature detector 
        orb = cv2.ORB_create(nfeatures = 1000)

        # Red filter on the picture
        res_r = cv2.bitwise_and(image_2, image_2, mask= mask_r)

        #Make a copy of the original image to display the keypoints found by ORB
        #This is just a representative
        preview_1 = np.copy(image_1)
        preview_2 = np.copy(res_r)
      
        #Create another copy to display points only
        dots = np.copy(image_1)

        #Extract the keypoints from both images
        train_keypoints, train_descriptor = orb.detectAndCompute(image_1, None)
        test_keypoints, test_descriptor = orb.detectAndCompute(res_r, None)

        #Draw the found Keypoints of the main image
        cv2.drawKeypoints(image_1, train_keypoints, preview_1, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.drawKeypoints(image_1, train_keypoints, dots, flags=2)

        try:
            #############################################
            ################## MATCHER ##################
            #############################################

            #Initialize the BruteForce Matcher
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

            #Match the feature points from both images
            matches = bf.match(train_descriptor, test_descriptor)
            
            #The matches with shorter distance are the ones we want.
            matches = sorted(matches, key = lambda x : x.distance)
        
            #Catch some of the matching points to draw
            good_matches = matches[:]

            #Parse the feature points
            train_points = np.float32([train_keypoints[m.queryIdx].pt for m in good_matches]).reshape(-1,1,2)
            test_points = np.float32([test_keypoints[m.trainIdx].pt for m in good_matches]).reshape(-1,1,2)

            #Create a mask to catch the matching points 
            #With the homography we are trying to find perspectives between two planes
            #Using the Non-deterministic RANSAC method
            M, mask = cv2.findHomography(train_points, test_points, cv2.RANSAC, 5.0)

            #Catch the width and height from the main image
            h,w = res_r.shape[:2]

            #Create a floating matrix for the new perspective
            pts = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)

            #Create the perspective in the result 
            dst = cv2.perspectiveTransform(pts,M)

            cv2.imshow('Img',image_2)
            cv2.imshow('Points',preview_1)
            cv2.imshow('Detection',res_r)       
        except:
            pass
        else:
            hsv = cv2.cvtColor(image_2, cv2.COLOR_BGR2HSV)
            h,s,v= cv2.split(hsv)
            ret, th = cv2.threshold(h,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

            # Remplissage des contours (quivalent  un oprateur morpho de Fermeture)
            im_floodfill = th.copy()
            h, w = th.shape[:2]
            mask = np.zeros((h+2, w+2), np.uint8)
            cv2.floodFill(im_floodfill, mask, (0,0), 255)
            im_floodfill_inv = cv2.bitwise_not(im_floodfill)
            th = th | im_floodfill_inv


            # Dtection des objets
            img_final, contours, hierarchy = cv2.findContours(th,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for i in range (0, len(contours)) :
                mask_BB_i = np.zeros((len(th),len(th[0])), np.uint8)
                x,y,w,h = cv2.boundingRect(contours[i])
                cv2.drawContours(mask_BB_i, contours, i, (255,255,255), -1)
                BB_i=cv2.bitwise_and(res_r,res_r,mask=mask_BB_i)
                cv2.imshow('mask_BB_i',mask_BB_i)   
            print("--------------")
            print("h: " + str(h))
            print("w: " + str(w))
            self.bottle_found(h, w)
        
        cv2.waitKey(1)

    def prove(self):
        for self.x in range(4,1001,18):
            for y in range (1,500):
                print (self.x)
                rospy.sleep(0.0001) 

def main():
    load_feature_object = LoadFeature()
    rospy.init_node('load_feature_node', anonymous=True)
    
    # load_feature_object.prove()
    try:
        rospy.spin()
        
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()