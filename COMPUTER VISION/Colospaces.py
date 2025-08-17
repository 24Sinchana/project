import os
import cv2

img=cv2.imread(os.path.join('.','birds.jpg'))

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #three channels to 1channels
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)  #HSV (Hue, Saturation, Value)
#switched the blue and red colors

cv2.imshow('img',img)
cv2.imshow('img_gray',img_gray)
cv2.imshow('img_rgb',img_rgb)
cv2.imshow('img_hsv',img_hsv)
cv2.waitKey(0)





