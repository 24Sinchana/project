import os
import cv2


img=cv2.imread(os.path.join('.','Dogs.jpg'))

cv2.imshow('img',img)
print(img.shape)

croped_img=img[120:600,160:800]

cv2.imshow('croped_img',croped_img)

print(croped_img.shape)
cv2.waitKey(0)






cv2.waitKey(0)
