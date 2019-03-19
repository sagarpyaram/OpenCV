import numpy as np
import cv2
cam=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('C:\\Users\\SAGAR\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\SAGAR\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')
i=0
while True:
    ret , img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    i=0
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        i=i+1
        m=str(i)
        #for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,m,(10,400), font, 4,(255,255,255),2,cv2.LINE_AA)
    i=0
    m=str(i)
    cv2.imshow("img",img)     
    if cv2.waitKey(3)==ord('q'):
        break; 
cam.release()
cv2.destroyAllWindows()
