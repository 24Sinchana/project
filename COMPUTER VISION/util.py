import numpy as np

import cv2

def get_limits(color):

    c = np.uint8([[color]]) #here insert the bgr value you want to cover

    hsvC=cv2.cvtColor(c,cv2.COLOR_BGR2HSV) #convert the image to hsv

    lowerlimit = hsvC[0][0][0] -10,100,100
    upperlimit = hsvC[0][0][0] +10,255,255

    lowerlimit = np.array(lowerlimit,dtype=np.uint8)
    upperlimit = np.array(upperlimit, dtype=np.uint8)

    return lowerlimit,upperlimit
