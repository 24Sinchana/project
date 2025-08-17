import os
import cv2

import numpy as np

img = cv2.imread(os.path.join('.', 'basketball.jpg'))



#edges = cv2.Canny(image, threshold1, threshold2)  syntax

img_edge = cv2.Canny(img,100,200)

img_edge_d = cv2.dilate(img_edge, np.ones((1,2),dtype = np.int8))

img_edge_e = cv2.erode(img_edge, np.ones((1,2),dtype = np.int8))

cv2.imshow('img',img)
cv2.imshow('img_edges',img_edge)
cv2.imshow('img_edges_d',img_edge_d)  
cv2.imshow('img_edges_e',img_edge_e)
cv2.waitKey(0)

