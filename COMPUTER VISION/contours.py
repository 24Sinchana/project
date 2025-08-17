import os
import cv2

#first convert the image to gray scale image and then add the threshold to the image
img = cv2.imread(os.path.join('.','fly.jpg'))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret , thresh = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)

#to find the contour in the image
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


for cnt in contours:
    if cv2.contourArea(cnt)>200:
        #cv2.drawContours(img, cnt, -1,(0, 255, 0 ),1)

        x1, y1, w , h = cv2.boundingRect(cnt) #bounding box is expressed as the upper right corner and then width and height
        cv2.rectangle(img,(x1,y1), (x1+w, y1+h), (0,255,0),2)

#x and y coridates with w and h
#contours Are drawn on the orginal image


cv2.imshow('img', img)
#cv2.imshow('img_gray', img_gray)
#cv2.imshow('thresh', thresh)

cv2.waitKey(0)

#convert the image to the threshold image while using the contours(binary)
#while working with contours we edit the contours,white isolated regions
#there we used the inverse threshold