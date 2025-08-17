import cv2

import os

video_path = os.path.join('.','data','humming_bird.mp4')

video = cv2.VideoCapture(video_path)


#Visualize the video
ret =True
while ret:

     ret, frame = video.read()
     #ret is the boolean variable that checks if the frame is read successfully or not.
     #when the frames in the video are not left at the end the ret becomes false.
     #frame is the actual frame reading from the video.

     if ret:

          cv2.imshow('frame',frame)
          cv2.waitKey(40)
video.release()
cv2.destroyAllWindows()

