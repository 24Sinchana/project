import os
import cv2
#convert the image into the Binary image using the gray scale


img=cv2.imread(os.path.join('.','bear.jpg'))

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray_img,80,255,cv2.THRESH_BINARY)

thresh = cv2.blur(thresh,(10,10))

ret,thresh = cv2.threshold(thresh,80,255,cv2.THRESH_BINARY)



cv2.imshow('img',img)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)

#above threshold will be white and other values below threshold will be black
