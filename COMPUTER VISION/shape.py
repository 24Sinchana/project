import os
import cv2


img= cv2.imread(os.path.join('.', 'white.png'))

print(img.shape)
#draw line on top of the image
cv2.line(img,  (20,155), (220,50) ,(0,255,0),3)


#rectange draw

#cv2.rectangle(img,(10,5),(90,129),(0,0,255),5)

cv2.rectangle(img,(100,20),(160,90),(0,0,255),-1)

#circle
cv2.circle(img,(230,80),25,(255,0,0),3)


cv2.putText(img,'hey!!',(30,130), cv2.FONT_HERSHEY_SIMPLEX,2.0,(255,0,0),2)








cv2.imshow('img',img)
cv2.waitKey(0)