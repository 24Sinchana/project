import os
import cv2

image_path = os.path.join('.','data','catss.jpg')

img=cv2.imread(image_path)
cv2.imwrite(os.path.join('.','data','catss_out.jpg'),img)

cv2.imshow('image',img)
cv2.waitKey(5000)  #milisec you want to keep the image open
#display image on the screen till any key is pressed


