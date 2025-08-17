import cv2

webcam = cv2.VideoCapture(0) #more than 2 web cam

#visualize webcam
while True:
    ret,frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):

      break

# It acts as a bitmask, ensuring that only the relevant information—the key code itself—is used for comparison


webcam.release()
cv2.destroyAllWindows()


