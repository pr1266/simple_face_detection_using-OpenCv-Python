import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while(True):

    #capture frame by frame

    ret , frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray , minNeighbors = 5)

    for x , y , w , h in faces:
        
        print(x , y , w , h)

        # region of interest
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # capture the image of last man detected 
        img_item = 'last_man.png'
        cv2.imwrite(img_item , roi_gray)

        #draw a rect

        # not a rgb color ! its BGR!
        color = (255 , 0 , 0)
        stroke = 2
        # initialize a end cord !
        width = x + w
        height = y + h
        cv2.rectangle(frame , (x , y) , (width , height) , color , stroke)

    #display resulting frame
    cv2.imshow('face detection designed by poorya' , frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()