import os
import argparse
import cv2
import mediapipe as np


def process_img(img,face_detection):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:

        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            # blur face
            img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (30, 30))  # cordinates of the face
    return img

args = argparse.ArgumentParser()

args.add_argument('--mode',default ='image')
args.add_argument('---filepath',default ='data/test.png')

args= args.parse_args()


output_dir ='./output'
# Check if the directory DOES NOT exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#detect faces
np_face_detection = np.solutions.face_detection

with np_face_detection.FaceDetection(min_detection_confidence=0.5,model_selection=0) as face_detection:

    if args.mode in ["image"]:

        img = cv2.imread(args.filepath)

        H,W,_ = img.shape
        img = process_img(img, face_detection)


        cv2.imwrite(os.path.join(output_dir,'output.png'),img)

    elif args.mode in['video']:
        cap = cv2.VideoCapture(args.filepath)
        ret,frame = cap.read()


        while True:
            frame = process_img(frame, face_detection)
            ret,frame = cap.read()


#save image