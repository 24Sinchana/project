import os
import cv2


img = cv2.imread(os.path.join('.', 'freelanc.jpg'))

k_size =11 #larger region
img_blur = cv2.blur(img,(k_size,k_size))
img_gauss=cv2.GaussianBlur(img,(k_size,k_size),3)
img_median_blured=cv2.medianBlur(img,(k_size))

cv2.imshow('img',img)
cv2.imshow('img_blur',img_blur)
cv2.imshow('img_gauss',img_gauss)
cv2.imshow('img_median_blured',img_median_blured)
cv2.waitKey(0)

#median_blur to remov ehe noice in the picture
#dpending on the type of the noice you have  in the image you use the blur function of openCV

