import os
import numpy

import cv2

img=cv2.imread(os.path.join('.', 'Dogs.jpg'))

resized_image = cv2.resize(img,(648,480))

print(img.shape)
print(resized_image.shape)



cv2.imshow('img',img)
cv2.imshow('resized',resized_image)


cv2.waitKey(0)