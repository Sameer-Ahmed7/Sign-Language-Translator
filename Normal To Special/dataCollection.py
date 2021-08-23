import cv2
import os
import time
import uuid

Image_Path = "E:/YoutubeSign v4/RealTimeObjectDetection/Tensorflow/workspace/images/collectedimages/"
#labels = ["Hello","Good Bye","Nice To Meet You","Yes","No","Thank You","Okay","Sorry","Please","Welcome"]
labels = ["Yes"]
number_imgs = 3

for label in labels:
    #os.mkdir("collectedImages/"+label)
    cap = cv2.VideoCapture(0)
    print("Collecting images for {}".format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(Image_Path,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        print(label+" "+str(imgnum))
        cv2.imwrite(imgname,frame)
        print("Picture Saved")
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,label, (10, 450), font, 3, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame',frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()